# frontend
from tkinter import *
from tkinter.messagebox import showinfo, askyesno
from tkinter.ttk import Notebook
import backend
import config
import re
from functools import partial


def int_number_field_valid(value):
    if value == "":
        return True
    try:
        value = int(value)
        return True
    except ValueError:
        return False


def float_number_field_valid(value):
    if value == "":
        return True
    try:
        value = float(value)
        return True
    except ValueError:
        return False


def phone_number_valid(value):
    if value == "":
        return True
    return re.fullmatch("^\+\d{0,11}", value) is not None

# def date_valid(value):
#     if value == "":
#         return True
#     return re.fullmatch("[0-9]{4}-[0-9]{2}-[0-9]{2}", value) is not None


class Frontend:
    def __init__(self, window):
        self.window = window
        self.__setup_window()

        self.database_created = False

        self.__setup_variables()

        main_frame = Frame(self.window, bg=config.background)
        main_frame.grid()

        notebook = Notebook(main_frame)
        notebook.pack(expand=True, fill=BOTH)

        vcmd_int = (self.window.register(int_number_field_valid))
        vcmd_float = (self.window.register(int_number_field_valid))
        vcmd_phone = (self.window.register(phone_number_valid))
        # vcmd_date = (self.window.register(date_valid))

        button_texts = ["Add New", "Clear", "Update", "Exit", "Delete"]

        self.seller_texts, self.seller_listbox = self.__setup_frame(
            notebook, "Sellers",
            ["Full Name", "Phone Number"],
            [(self.SellerFullName, None),
             (self.SellerPhoneNumber, vcmd_phone)], button_texts,
            [self.add_seller_data, partial(self.clear_data, [self.SellerFullName, self.SellerPhoneNumber]), self.update_seller, self.exit, self.deleteDatabase], self.get_seller)

        self.customer_texts, self.customer_listbox = self.__setup_frame(
            notebook, "Customers",
            ["Full Name", "Phone Number"],
            [(self.CustomerFullName, None),
             (self.CustomerPhoneNumber, vcmd_phone)], button_texts,
            [self.add_customer_data, partial(self.clear_data, [self.CustomerFullName, self.CustomerPhoneNumber]), self.update_customer, self.exit, self.deleteDatabase], self.get_customer)

        self.payment_texts, self.payment_listbox = self.__setup_frame(
            notebook, "Payments",
            ["Payment Method", "Payment Date", "Account", "Payment Size"],
            [(self.PaymentMethod, None), (self.PaymentDate, None), (self.PaymentAccountNumber, None), (self.PaymentReceiptSize, vcmd_float)], button_texts,
            [self.add_payment_data, partial(self.clear_data, [self.PaymentMethod, self.PaymentDate, self.PaymentAccountNumber, self.PaymentReceiptSize]),
             self.update_payment, self.exit, self.deleteDatabase], self.get_payment)

        self.automobile_texts, self.automobile_listbox = self.__setup_frame(
            notebook, "Automobiles",
            ["Model Name", "Color", "Number of seats", "Engine"],
            [(self.ModelName, None), (self.ModelColour, None),
             (self.ModelNumberOfSeats, vcmd_int), (self.ModelEngine, None)], button_texts,
            [self.add_automobile_data, partial(self.clear_data, [self.ModelName, self.ModelColour, self.ModelNumberOfSeats, self.ModelEngine]),
             self.update_automobile, self.exit, self.deleteDatabase], self.get_automobile)

        tables = [("seller", self.seller_listbox),
                  ("customer", self.customer_listbox),
                  ("payment", self.payment_listbox),
                  ("model", self.automobile_listbox)]

        for i in range(len(tables)):
            table_name, listbox = tables[i]
            self.open_table(listbox, table_name)

    def open_table(self, listbox, table_name):
        data = backend.view_data(table_name)
        if not data:
            #backend.testFilling()
            return
        listbox.delete(0, END)
        for row in data:
            listbox.insert(END, row)
        self.database_created = True

    def createNewDatabase(self):
        if self.database_created:
            creating = askyesno(
                config.title, "Are you sure you want to recreate database?\n The old one will be deleted!")
        else:
            creating = True
        if creating:
            # backend.dropDealershipDB()
            backend.create_dealership_db()
            if self.database_created:
                showinfo("Action", "Database has been created.")
            self.database_created = True
        else:
            showinfo("Action", "Action canceled")

    def deleteDatabase(self):
        deleting = askyesno(
            config.title, "Are you sure you want to delete database?")
        if deleting > 0:
            backend.drop_dealership_db()
            self.database_created = False
            showinfo("Action", "Database has been deleated.")

    def clear_database(self):
        backend.clear_database()

    def exit(self):
        exiting = askyesno(config.title, "Confirm if you want to exit")
        if exiting:
            self.window.destroy()

    def add_seller_data(self):
        self.database_created = True
        backend.add_data_seller(self.SellerFullName.get(),
                                self.SellerPhoneNumber.get())
        self.seller_listbox.insert(
            END, (self.SellerFullName.get(), self.SellerPhoneNumber.get()))

    def add_customer_data(self):
        self.database_created = True
        backend.add_data_customer(
            self.CustomerFullName.get(), self.CustomerPhoneNumber.get())
        self.customer_listbox.insert(
            END, (self.CustomerFullName.get(), self.CustomerPhoneNumber.get()))

    def add_payment_data(self):
        self.database_created = True
        backend.add_data_payment(
            self.PaymentMethod.get(),
            self.PaymentDate.get(),
            self.PaymentAccountNumber.get(),
            self.PaymentReceiptSize.get())
        self.payment_listbox.insert(
            END,
            (self.PaymentMethod.get(),
             self.PaymentDate.get(),
             self.PaymentAccountNumber.get(),
             self.PaymentReceiptSize.get()))

    def add_automobile_data(self):
        self.database_created = True
        backend.add_data_model(
            self.ModelName.get(),
            self.ModelColour.get(),
            self.ModelNumberOfSeats.get(),
            self.ModelEngine.get())
        self.automobile_listbox.insert(
            END,
            (self.ModelName.get(),
             self.ModelColour.get(),
             self.ModelNumberOfSeats.get(),
             self.ModelEngine.get()))

    def update_seller(self):
        self.seller_listbox.delete(0, END)
        if self.database_created:
            data = backend.view_data("seller")
            self.seller_listbox.delete(0, END)
            for row in data:
                self.seller_listbox.insert(END, row)

    def update_customer(self):
        self.customer_listbox.delete(0, END)
        if self.database_created:
            data = backend.view_data("customer")
            self.customer_listbox.delete(0, END)
            for row in data:
                self.customer_listbox.insert(END, row)

    def update_payment(self):
        self.payment_listbox.delete(0, END)
        if self.database_created:
            data = backend.view_data("payment")
            self.payment_listbox.delete(0, END)
            for row in data:
                self.payment_listbox.insert(END, row)

    def update_automobile(self):
        self.automobile_listbox.delete(0, END)
        if self.database_created:
            data = backend.view_data("model")
            self.automobile_listbox.delete(0, END)
            for row in data:
                self.automobile_listbox.insert(END, row)

    def get_seller(self, event):
        search_seller = self.seller_listbox.curselection()
        if not search_seller:
            return

        seller = self.seller_listbox.get(search_seller[0])

        # Обновление в полях ввода
        for i in range(len(self.seller_texts)):
            self.seller_texts[i].delete(0, END)
            self.seller_texts[i].insert(END, seller[i + 1]) # skip id

    def get_customer(self, event):
        search = self.customer_listbox.curselection()
        if not search:
            return

        customer = self.customer_listbox.get(search[0])

        # Обновление в полях ввода
        for i in range(len(self.customer_texts)):
            self.customer_texts[i].delete(0, END)
            self.customer_texts[i].insert(END, customer[i + 1]) # skip id

    def get_payment(self, event):
        search = self.payment_listbox.curselection()
        if not search:
            return

        payment = self.payment_listbox.get(search[0])

        # Обновление в полях ввода
        for i in range(len(self.payment_texts)):
            self.payment_texts[i].delete(0, END)
            self.payment_texts[i].insert(END, payment[i + 1]) # skip id

    def get_automobile(self, event):
        search = self.automobile_listbox.curselection()
        if not search:
            return

        automobile = self.automobile_listbox.get(search[0])

        # Обновление в полях ввода
        for i in range(len(self.automobile_texts)):
            self.automobile_texts[i].delete(0, END)
            self.automobile_texts[i].insert(END, automobile[i + 1]) # skip id


    def clear_data(self, variables_list):
        for i in range(len(variables_list)):
            variables_list[i].set("")

    def __setup_window(self):
        self.window.title(config.title)
        self.window.geometry(config.resolution)
        self.window.config(bg=config.background)
        # self.window.resizable(0, 0)

    def __setup_variables(self):
        # Seller
        self.SellerFullName = StringVar()
        self.SellerPhoneNumber = StringVar()

        # Customer
        self.CustomerFullName = StringVar()
        self.CustomerPhoneNumber = StringVar()

        # Maker
        self.MakerCountry = StringVar()
        self.MakerCompany = StringVar()

        # Model
        self.ModelName = StringVar()
        self.ModelColour = StringVar()
        self.ModelNumberOfSeats = IntVar()
        self.ModelEngine = StringVar()

        # Price
        self.PriceModelId = IntVar()
        self.PriceValue = DoubleVar()
        self.PriceDateFrom = StringVar()
        self.PriceDateTo = StringVar()

        # Automobile
        self.AutomobileBrand = StringVar()

        # Payment
        self.PaymentMethod = StringVar()
        self.PaymentDate = StringVar()
        self.PaymentAccountNumber = StringVar()
        self.PaymentReceiptSize = DoubleVar()

        # Service_info
        self.SIServiceDate = StringVar()

    def __setup_frame(self, notebook, notebook_label, label_texts, text_variables, button_texts, commands, list_command):
        data_frame = Frame(notebook, borderwidth=2, padx=20,
                           pady=20, width=1000, height=400, relief=RIDGE, bg=config.background)
        data_frame.pack(side=BOTTOM)

        button_frame = Frame(data_frame, borderwidth=2, padx=20,
                             pady=10, width=1350, height=70, relief=RIDGE, bg=config.text_background)
        button_frame.pack(side=BOTTOM)

        data_frame_left = LabelFrame(data_frame, bd=1, width=600, height=600, padx=20, relief=RIDGE,
                                     bg=config.text_background, font=(config.font, 26, 'bold'), text="Table Info\n")
        data_frame_left.pack(side=LEFT)
        data_frame_right = LabelFrame(data_frame, bd=1, width=450, height=450, padx=31, pady=3, relief=RIDGE,
                                      bg=config.text_background, font=(config.font, 20, 'bold'), text="Table Data\n")
        data_frame_right.pack(side=RIGHT)

        labels = []
        entries = []

        for i in range(len(label_texts)):
            labels.append(Label(data_frame_left, font=(
                config.font, 20, 'bold'), text=label_texts[i], padx=2, pady=2, bg=config.text_background))
            labels[i].grid(row=i, column=0, sticky=W)

            variable, validator = text_variables[i]

            if validator is not None:
                entries.append(Entry(data_frame_left, font=(
                    config.font, 20, 'bold'), textvariable=variable, width=39, validate="all", validatecommand=(validator, "%P")))
            else:
                entries.append(Entry(data_frame_left, font=(
                    config.font, 20, 'bold'), textvariable=variable, width=39))
            entries[i].grid(row=i, column=1)

        scrollbar = Scrollbar(data_frame_right)
        scrollbar.grid(row=0, column=1, sticky='ns')

        list_box = Listbox(data_frame_right, width=45, height=16, font=(
            config.font, 12, 'bold'), yscrollcommand=scrollbar.set)
        list_box.bind('<<ListboxSelect>>', list_command)
        list_box.grid(row=0, column=0, padx=8)

        scrollbar.config(command=list_box.yview)

        buttons = []

        for i in range(len(button_texts)):
            buttons.append(Button(button_frame, text=button_texts[i], font=(
                config.font, 20, 'bold'), height=1, width=10, bd=4, command=commands[i]))
            buttons[i].grid(row=0, column=i)

        notebook.add(data_frame, text=notebook_label)

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
