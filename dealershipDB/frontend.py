"""
frontend
"""
import re
from functools import partial
# pylint: disable=unused-wildcard-import
from tkinter import *  # pylint: disable=wildcard-import
from tkinter.messagebox import askyesno, showinfo
from tkinter.ttk import Notebook

import backend
import config


def int_number_field_valid(value):
    """
    checks whether the value can be converted to int
    """
    if value == "":
        return True
    try:
        value = int(value)
        return True
    except ValueError:
        return False


def float_number_field_valid(value):
    """
    checks whether the value can be converted to float
    """
    if value == "":
        return True
    try:
        value = float(value)
        return True
    except ValueError:
        return False


def phone_number_valid(value):
    """
    checks if the phone number is valid
    """
    if value == "":
        return True
    return re.fullmatch("^\\+\\d{0,11}", value) is not None

def date_valid(value):
    """
    checks if date is valid
    """
    if value == "":
        return True
    return re.fullmatch("\\d{,4}-?\\d{,2}-?\\d{,2}", value) is not None


class Frontend:
    """
    main frontend class to work with windows
    """

    # pylint: disable=too-many-instance-attributes

    def __init__(self, window):
        self.window = window
        self.__setup_window()

        self.database_created = False

        self.__setup_variables()

        main_frame = Frame(self.window, bg=config.BACKGROUND)

        notebook = Notebook(main_frame)

        vcmd_int = self.window.register(int_number_field_valid)
        vcmd_float = self.window.register(int_number_field_valid)
        vcmd_phone = self.window.register(phone_number_valid)
        vcmd_date = self.window.register(date_valid)

        button_texts = ["Add New", "Clear", "Update", "Exit", "Delete"]

        self.seller_texts, self.seller_listbox = self.__setup_frame(
            notebook, "Sellers",
            ["Full Name", "Phone Number"],
            [(self.seller_full_name, None),
             (self.seller_phone_number, vcmd_phone)],
            button_texts,
            [self.add_seller_data,
             partial(self.clear_data, [self.seller_full_name, self.seller_phone_number]),
             self.update_seller, self.exit, self.delete_database],
            self.get_seller)

        self.customer_texts, self.customer_listbox = self.__setup_frame(
            notebook, "Customers",
            ["Full Name", "Phone Number"],
            [(self.customer_full_name, None),
             (self.customer_phone_number, vcmd_phone)],
            button_texts,
            [self.add_customer_data,
             partial(self.clear_data, [self.customer_full_name, self.customer_phone_number]),
             self.update_customer, self.exit, self.delete_database],
            self.get_customer)

        self.payment_texts, self.payment_listbox = self.__setup_frame(
            notebook, "Payments",
            ["Payment Method", "Payment Date", "Account", "Payment Size"],
            [(self.payment_method, None), (self.payment_date, vcmd_date),
             (self.payment_account_number, None), (self.payment_receipt_size, vcmd_float)],
            button_texts,
            [self.add_payment_data,
             partial(self.clear_data,
                     [self.payment_method, self.payment_date,
                      self.payment_account_number, self.payment_receipt_size]),
             self.update_payment, self.exit, self.delete_database],
            self.get_payment)

        self.automobile_texts, self.automobile_listbox = self.__setup_frame(
            notebook, "Automobiles",
            ["Model Name", "Color", "Number of seats", "Engine"],
            [(self.model_name, None), (self.model_colour, None),
             (self.model_number_of_seats, vcmd_int), (self.model_engine, None)],
            button_texts,
            [self.add_automobile_data,
             partial(self.clear_data, [self.model_name, self.model_colour,
                                       self.model_number_of_seats, self.model_engine]),
             self.update_automobile, self.exit, self.delete_database],
            self.get_automobile)

        tables = [("seller", self.seller_listbox),
                  ("customer", self.customer_listbox),
                  ("payment", self.payment_listbox),
                  ("model", self.automobile_listbox)]

        for table in tables:
            table_name, listbox = table
            self.open_table(listbox, table_name)

        main_frame.pack()

        notebook.pack()

        self.window.update()

    def open_table(self, listbox, table_name):
        """
        opens a table
        """
        data = backend.view_data(table_name)
        if not data:
            backend.test_filling()
            return
        listbox.delete(0, END)
        for row in data:
            listbox.insert(END, row)
        self.database_created = True

    def create_new_database(self):
        """
        creates new database
        """
        if self.database_created:
            creating = askyesno(
                config.TITLE,
                "Are you sure you want to recreate database?\n The old one will be deleted!")
        else:
            creating = True
        if creating:
            backend.create_dealership_db()
            if self.database_created:
                showinfo("Action", "Database has been created.")
            self.database_created = True
        else:
            showinfo("Action", "Action canceled")

    def delete_database(self):
        """
        deletes database
        """
        deleting = askyesno(
            config.TITLE, "Are you sure you want to delete database?")
        if deleting > 0:
            backend.drop_dealership_db()
            self.database_created = False
            showinfo("Action", "Database has been deleated.")

    def clear_database(self):
        """
        clears data
        """
        backend.clear_database()

    def exit(self):
        """
        exiting the program
        """
        exiting = askyesno(config.TITLE, "Confirm if you want to exit")
        if exiting:
            self.window.destroy()

    def add_seller_data(self):
        """
        adds data to table seller
        """
        self.database_created = True
        if backend.add_data_seller(
                self.seller_full_name.get(),
                self.seller_phone_number.get()):
            self.update_seller()

    def add_customer_data(self):
        """
        adds data to table customer
        """
        self.database_created = True
        if backend.add_data_customer(
                self.customer_full_name.get(),
                self.customer_phone_number.get()):
            self.update_customer()

    def add_payment_data(self):
        """
        adds data to table payment
        """
        self.database_created = True
        if backend.add_data_payment(
                self.payment_method.get(),
                self.payment_date.get(),
                self.payment_account_number.get(),
                self.payment_receipt_size.get()):
            self.update_payment()

    def add_automobile_data(self):
        """
        adds data to table automobile
        """
        self.database_created = True
        if backend.add_data_model(
                self.model_name.get(),
                self.model_colour.get(),
                self.model_number_of_seats.get(),
                self.model_engine.get()):
            self.update_automobile()

    def update_seller(self):
        """
        update seller data
        """
        self.seller_listbox.delete(0, END)
        if self.database_created:
            data = backend.view_data("seller")
            self.seller_listbox.delete(0, END)
            for row in data:
                self.seller_listbox.insert(END, row)

    def update_customer(self):
        """
        update customer data
        """
        self.customer_listbox.delete(0, END)
        if self.database_created:
            data = backend.view_data("customer")
            self.customer_listbox.delete(0, END)
            for row in data:
                self.customer_listbox.insert(END, row)

    def update_payment(self):
        """
        update payment data
        """
        self.payment_listbox.delete(0, END)
        if self.database_created:
            data = backend.view_data("payment")
            self.payment_listbox.delete(0, END)
            for row in data:
                self.payment_listbox.insert(END, row)

    def update_automobile(self):
        """
        update automobile data
        """
        self.automobile_listbox.delete(0, END)
        if self.database_created:
            data = backend.view_data("model")
            self.automobile_listbox.delete(0, END)
            for row in data:
                self.automobile_listbox.insert(END, row)

    def get_seller(self, event):  # pylint: disable=unused-argument
        """
        gets seller data
        """
        search_seller = self.seller_listbox.curselection()
        if not search_seller:
            return

        seller = self.seller_listbox.get(search_seller[0])

        # Обновление в полях ввода
        for i, _ in enumerate(self.seller_texts):
            self.seller_texts[i].delete(0, END)
            self.seller_texts[i].insert(END, seller[i + 1])  # skip id

    def get_customer(self, event):  # pylint: disable=unused-argument
        """
        gets customer data
        """
        search = self.customer_listbox.curselection()
        if not search:
            return

        customer = self.customer_listbox.get(search[0])

        # Обновление в полях ввода
        for i, _ in enumerate(self.customer_texts):
            self.customer_texts[i].delete(0, END)
            self.customer_texts[i].insert(END, customer[i + 1])  # skip id

    def get_payment(self, event):  # pylint: disable=unused-argument
        """
        gets payment data
        """
        search = self.payment_listbox.curselection()
        if not search:
            return

        payment = self.payment_listbox.get(search[0])

        # Обновление в полях ввода
        for i, _ in enumerate(self.payment_texts):
            self.payment_texts[i].delete(0, END)
            self.payment_texts[i].insert(END, payment[i + 1])  # skip id

    def get_automobile(self, event):  # pylint: disable=unused-argument
        """
        gets automobile data
        """
        search = self.automobile_listbox.curselection()
        if not search:
            return

        automobile = self.automobile_listbox.get(search[0])

        # Обновление в полях ввода
        for i, _ in enumerate(self.automobile_texts):
            self.automobile_texts[i].delete(0, END)
            self.automobile_texts[i].insert(END, automobile[i + 1])  # skip id

    def clear_data(self, variables_list):
        """
        clears data
        """
        for variable in variables_list:
            variable.set("")

    def __setup_window(self):
        self.window.title(config.TITLE)
        self.window.geometry(config.RESOLUTION)
        self.window.config(bg=config.BACKGROUND)
        self.window.protocol("WM_DELETE_WINDOW",self.exit)
        self.window.resizable(0, 0)

    def __setup_variables(self):
        # Seller
        self.seller_full_name = StringVar()
        self.seller_phone_number = StringVar()

        # Customer
        self.customer_full_name = StringVar()
        self.customer_phone_number = StringVar()

        # Maker
        self.make_country = StringVar()
        self.maker_company = StringVar()

        # Model
        self.model_name = StringVar()
        self.model_colour = StringVar()
        self.model_number_of_seats = IntVar()
        self.model_engine = StringVar()

        # Price
        self.price_value = DoubleVar()
        self.price_date_from = StringVar()
        self.price_date_to = StringVar()

        # Automobile
        self.automobile_brand = StringVar()

        # Payment
        self.payment_method = StringVar()
        self.payment_date = StringVar()
        self.payment_account_number = StringVar()
        self.payment_receipt_size = DoubleVar()

        # Service_info
        self.si_service_date = StringVar()

    def __setup_frame(  # pylint: disable=too-many-arguments
                        # pylint: disable=too-many-locals
            self,
            notebook,
            notebook_label,
            label_texts,
            text_variables,
            button_texts,
            commands,
            list_command
            ):
        page_frame = Frame(notebook, borderwidth=2, padx=20,
                           pady=20, relief=RIDGE, bg=config.BACKGROUND)
        data_frame = Frame(page_frame, borderwidth=2, padx=20,
                           pady=20, bg=config.BACKGROUND)

        button_frame = Frame(page_frame, borderwidth=2, padx=20,
                             pady=10, relief=RIDGE, bg=config.TEXT_BACKGROUND)

        data_frame_left = LabelFrame(
            data_frame,
            bd=1,
            padx=20,
            relief=RIDGE,
            bg=config.TEXT_BACKGROUND,
            font=(config.FONT, 26, 'bold'),
            text="Table Info\n"
            )

        data_frame_right = LabelFrame(
            data_frame,
            bd=1,
            relief=RIDGE,
            bg=config.TEXT_BACKGROUND,
            font=(config.FONT, 20, 'bold'),
            text="Table Data\n"
            )

        labels = []
        entries = []

        for i, _ in enumerate(label_texts):
            labels.append(Label(data_frame_left, font=(
                config.FONT, 20, 'bold'), text=label_texts[i],
                padx=2, pady=2, bg=config.TEXT_BACKGROUND))
            labels[i].grid(row=i, column=0, sticky=W)

            variable, validator = text_variables[i]

            if validator is not None:
                entries.append(Entry(data_frame_left, font=(
                    config.FONT, 20, 'bold'), textvariable=variable,
                    width=39, validate="all", validatecommand=(validator, "%P")))
            else:
                entries.append(Entry(data_frame_left, font=(
                    config.FONT, 20, 'bold'), textvariable=variable, width=39))
            entries[i].grid(row=i, column=1)

        list_box = Listbox(data_frame_right, width=70, height=16, font=(
            config.FONT, 12, 'bold'))
        list_box.bind('<<ListboxSelect>>', list_command)

        xscrollbar = Scrollbar(data_frame_right, orient=HORIZONTAL)
        xscrollbar.config(command=list_box.xview)

        yscrollbar = Scrollbar(data_frame_right, orient=VERTICAL)
        yscrollbar.pack(fill=Y, side=RIGHT)
        yscrollbar.config(command=list_box.yview)

        list_box["xscrollcommand"] = xscrollbar.set
        list_box["yscrollcommand"] = yscrollbar.set

        xscrollbar.pack(fill=X, side=BOTTOM)

        yscrollbar.pack(fill=Y, side=RIGHT)

        list_box.pack()

        buttons = []

        for i, butt_val in enumerate(button_texts):
            buttons.append(Button(button_frame, text=butt_val, font=(
                config.FONT, 20, 'bold'), height=1, width=10, bd=4, command=commands[i]))
            buttons[i].grid(row=0, column=i)

        data_frame_right.pack(side=RIGHT)

        data_frame_left.pack(side=LEFT)

        button_frame.pack(side=BOTTOM)

        data_frame.pack()

        page_frame.pack()

        notebook.add(page_frame, text=notebook_label)

        return entries, list_box

    # def get_from_list(self, list_box, text_variables, event):
    #     search = list_box.curselection()
    #     if not search:
    #         return

    #     found = list_box.get(search[0])

    #     # Обновление в полях ввода
    #     for i in range(len(text_variables)):
    #         text_variables[i].delete(0, END)
    #         text_variables[i].inster(END, found[i])
