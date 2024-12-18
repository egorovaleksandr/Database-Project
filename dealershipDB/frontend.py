#frontend
from tkinter import *
from tkinter.messagebox import showinfo, askyesno
from tkinter.ttk import Notebook
import backendDB
import config
import re

def numberFieldValid(value):
    if value == "":
        return True
    try:
        value = int(value)
        return True
    except ValueError:
        return False
    
def phoneNumberValid(value):
    if value == "":
        return True
    return re.match("^\+\d{0,11}$", value) is not None

class Frontend:
    def __init__(self, window):
        self.window = window
        self.__setupWindow()

        self.databaseCreated = False

        self.__setupVariables()

        mainFrame = Frame(self.window, bg=config.background)
        mainFrame.grid()

        notebook = Notebook(mainFrame)
        notebook.pack(expand=True, fill=BOTH)

        self.__setupSellerFrame(notebook)
        self.__setupCustomerFrame(notebook)

        self.openDatabase("seller")


    def exit(self):
        exiting = askyesno(config.title, "Confirm if you want to exit")
        if exiting:
            self.window.destroy()
    
    def addDataSeller(self):
        self.databaseCreated = True
        backendDB.addDataSeller(self.SellerFullName.get(), self.SellerPhoneNumber.get())
        self.SellerList.insert(END, (self.SellerID.get(), self.SellerFullName.get(), self.SellerPhoneNumber.get()))

    def addDataCustomer(self):
        self.databaseCreated = True
        backendDB.addDataCustomer(self.CustomerFullName.get(), self.CustomerPhoneNumber.get())
        self.CustomerList.insert(END, (self.CustomerID.get(), self.CustomerFullName.get(), self.CustomerPhoneNumber.get()))

    def openDatabase(self, tableName):
        data = backendDB.viewData(tableName)
        if not data:
            self.createNewDatabase()
            self.databaseCreated = True
            return
        self.SellerList.delete(0, END)
        for row in data:
            self.SellerList.insert(END, row)
        self.databaseCreated = True

    def createNewDatabase(self):
        if self.databaseCreated:
            creating = askyesno(config.title, "Are you sure you want to recreate database?\n The old one will be deleted!")
        else: 
            creating = True
        if creating:
            #backendDB.dropDealershipDB()
            backendDB.createDealershipDB()
            if self.databaseCreated:
                showinfo("Action", "Database has been created.")
            self.databaseCreated = True
        else:
            showinfo("Action", "Action canceled")

    def deleteDatabase(self):
        deleting = askyesno(config.title, "Are you sure you want to delete database?")
        if deleting > 0 :
            backendDB.dropDealershipDB()
            self.databaseCreated = False
            showinfo("Action", "Database has been deleated.")

    def updateSeller(self):
        self.SellerList.delete(0, END)
        if self.databaseCreated:
            data = backendDB.viewData("seller")
            self.SellerList.delete(0, END)
            for row in data:
                self.SellerList.insert(END, row)

    def updateCustomer(self):
        self.CustomerList.delete(0, END)
        if self.databaseCreated:
            data = backendDB.viewData("customer")
            self.CustomerList.delete(0, END)
            for row in data:
                self.CustomerList.insert(END, row)

    def clearData(self):
        self.SellerID.set(0)
        self.SellerFullName.set("")
        self.SellerPhoneNumber.set("")
        self.CustomerID.set(0)
        self.CustomerFullName.set("")
        self.CustomerPhoneNumber.set("")
    
    def __setupWindow(self):
        self.window.title(config.title)
        self.window.geometry(config.resolution)
        self.window.config(bg=config.background)
        self.window.resizable(0, 0)

    def __setupVariables(self):
        #Seller
        self.SellerID = IntVar()
        self.SellerFullName = StringVar()
        self.SellerPhoneNumber = StringVar()

        #Customer
        self.CustomerID = IntVar()
        self.CustomerFullName = StringVar()
        self.CustomerPhoneNumber = StringVar()

        #Maker
        self.MakerID = IntVar()
        self.MakerCountry = StringVar()
        self.MakerCompany = StringVar()

        #Model
        self.ModelId = IntVar()
        self.ModelName = StringVar()
        self.ModelColour = StringVar()
        self.ModelNumberOfSeats = IntVar()
        self.ModelEngine = StringVar()

        #Price
        self.PriceModelId = IntVar()
        self.PriceValue = DoubleVar()
        self.PriceDateFrom = StringVar()
        self.PriceDateTo = StringVar()

        #Automobile
        self.AutomobileID = IntVar()
        self.AutomobileBrand = StringVar()
        self.AutomobileMakerID = IntVar()
        self.AutomobileModelID = IntVar()

        #Payment
        self.PaymentID = IntVar()
        self.PaymentMethod = StringVar()
        self.PaymentDate = StringVar()
        self.PaymentAccountNumber = StringVar()
        self.PaymentReceiptSize = DoubleVar()

        #Service_info
        self.SIServiceID = IntVar()
        self.SISellerID = IntVar()
        self.SIAutomobileID = IntVar()
        self.SIServiceDate = StringVar()
        self.SIPayID = IntVar()

        #Service
        self.ServiceCustomerID = IntVar()
        self.serviceID = IntVar()
        self.ServiceAutomobileID = IntVar()

    def __setupSellerFrame(self, notebook):
        # titleFrame = Frame(mainFrame, bd=2, padx=54,pady=8, bg=config.text_background, relief=RIDGE)
        # titleFrame.pack(side=TOP)
        # labelTitle = Label(titleFrame, font=(config.font, 48, 'bold'), text="Car Dealership Database", bg=config.text_background)
        # labelTitle.grid()

        DataFrames = []
        DataFramesLEFT = []
        DataFramesRIGHT = []

        # tablesInfo = ...

        # for i in range(3):
            # newDataFrame = Frame(notebook, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE,bg=config.background)
            # newDataFrameLEFT = ...
            # newDataFrameRIGHT = ...

            #DataFrames.append(newDataFrame)
            #DataFramesLEFT.append(newDataFrameLEFT)
            #DataFramesRIGHT.append(newDataFrameRIGHT)


        # Seller
      

        # TODO: Выше сделать цикл по аналогии с тем, что ниже
        DataFrame = Frame(notebook, bd=1, width=1000, height=400, padx=20, pady=20, relief=RIDGE,bg=config.background)
        DataFrame.pack(side=BOTTOM)

        ButtonFrame = Frame(DataFrame, bd=2, width=1350, height=70, padx=19, pady=10, bg=config.text_background, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg=config.text_background, font=(config.font, 26, 'bold'), text="Table Info\n")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,bg=config.text_background,font=(config.font, 20, 'bold'),text="Table Data\n")
        DataFrameRIGHT.pack(side=RIGHT)

        vcmd = (self.window.register(numberFieldValid))
        vcmd_phone = (self.window.register(phoneNumberValid))

        self.labelSellerID = Label(DataFrameLEFT, font=(config.font, 20, 'bold'), text="Seller's ID:",padx=2,pady=2,bg=config.text_background)
        self.labelSellerID.grid(row=0,column=0,sticky=W)

        self.textSellerID = Entry(DataFrameLEFT, font=(config.font, 20, 'bold'), textvariable=self.SellerID, width=39, validate="all", validatecommand=(vcmd, "%P"))
        self.textSellerID.grid(row=0, column=1)

        self.labelSellerFullName = Label(DataFrameLEFT, font=(config.font, 20, 'bold'), text="Full Name:", padx=2, pady=2,bg=config.text_background)
        self.labelSellerFullName.grid(row=1, column=0, sticky=W)
        self.textSellerFullName = Entry(DataFrameLEFT, font=(config.font, 20, 'bold'), textvariable=self.SellerFullName, width=39)
        self.textSellerFullName.grid(row=1, column=1)

        self.labelSellerPhoneNumber = Label(DataFrameLEFT, font=(config.font, 20, 'bold'), text="Phone Number", padx=2, pady=2,bg=config.text_background)
        self.labelSellerPhoneNumber.grid(row=2, column=0, sticky=W)
        self.textSellerPhoneNumber = Entry(DataFrameLEFT, font=(config.font, 20, 'bold'), textvariable=self.SellerPhoneNumber, width=39, validate="all", validatecommand=(vcmd_phone, "%P"))
        self.textSellerPhoneNumber.grid(row=2, column=1)

        scrollbar= Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        self.SellerList = Listbox(DataFrameRIGHT, width=41, height=16, font=(config.font, 12, 'bold'),yscrollcommand=scrollbar.set)
        self.SellerList.bind('<<ListboxSelect>>', self.__getSeller)
        self.SellerList.grid(row=0, column=0, padx=8)
        scrollbar.config(command=self.SellerList.yview)

        buttonCreateTable = Button(ButtonFrame, text="Add New", font=(config.font, 20, 'bold'), height=1, width=10, bd=4, command=self.addDataSeller)
        buttonCreateTable.grid(row=0, column = 0)

        buttonClearData = Button(ButtonFrame, text="Clear", font=(config.font, 20, 'bold'), height=1, width=10, bd=4,command=self.clearData)
        buttonClearData.grid(row=0, column=1)

        buttonUpdateData = Button(ButtonFrame, text="Update", font=(config.font, 20, 'bold'), height=1, width=10, bd=4,command=self.updateSeller)
        buttonUpdateData.grid(row=0, column=2)

        buttonExit = Button(ButtonFrame, text="Exit", font=(config.font, 20, 'bold'), height=1, width=10, bd=4, command=self.exit)
        buttonExit.grid(row=0, column=3)

        btnDeleteData = Button(ButtonFrame, text="Delete", font=(config.font, 20, 'bold'), height=1, width=10, bd=4,command=self.deleteDatabase)
        btnDeleteData.grid(row=0, column=9)

        notebook.add(DataFrame, text="Seller")

    def __setupCustomerFrame(self, notebook):
        DataFrames = []
        DataFramesLEFT = []
        DataFramesRIGHT = []
    

        # TODO: Выше сделать цикл по аналогии с тем, что ниже
        DataFrame = Frame(notebook, bd=1, width=1000, height=400, padx=20, pady=20, relief=RIDGE,bg=config.background)
        DataFrame.pack(side=BOTTOM)

        ButtonFrame = Frame(DataFrame, bd=2, width=1350, height=70, padx=19, pady=10, bg=config.text_background, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg=config.text_background, font=(config.font, 26, 'bold'), text="Table Info\n")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,bg=config.text_background,font=(config.font, 20, 'bold'),text="Table Data\n")
        DataFrameRIGHT.pack(side=RIGHT)

        vcmd = (self.window.register(numberFieldValid))
        vcmd_phone = (self.window.register(phoneNumberValid))

        self.labelCustomerID = Label(DataFrameLEFT, font=(config.font, 20, 'bold'), text="Customers's ID:",padx=2,pady=2,bg=config.text_background)
        self.labelCustomerID.grid(row=0,column=0,sticky=W)

        self.textCustomerID = Entry(DataFrameLEFT, font=(config.font, 20, 'bold'), textvariable=self.CustomerID, width=39, validate="all", validatecommand=(vcmd, "%P"))
        self.textCustomerID.grid(row=0, column=1)

        self.labelCustomerFullName = Label(DataFrameLEFT, font=(config.font, 20, 'bold'), text="Full Name:", padx=2, pady=2,bg=config.text_background)
        self.labelCustomerFullName.grid(row=1, column=0, sticky=W)
        self.textCustomerFullName = Entry(DataFrameLEFT, font=(config.font, 20, 'bold'), textvariable=self.CustomerFullName, width=39)
        self.textCustomerFullName.grid(row=1, column=1)

        self.labelCustomerPhoneNumber = Label(DataFrameLEFT, font=(config.font, 20, 'bold'), text="Phone Number", padx=2, pady=2,bg=config.text_background)
        self.labelCustomerPhoneNumber.grid(row=2, column=0, sticky=W)
        self.textCustomerPhoneNumber = Entry(DataFrameLEFT, font=(config.font, 20, 'bold'), textvariable=self.CustomerPhoneNumber, width=39, validate="all", validatecommand=(vcmd_phone, "%P"))
        self.textCustomerPhoneNumber.grid(row=2, column=1)

        scrollbar= Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        self.CustomerList = Listbox(DataFrameRIGHT, width=41, height=16, font=(config.font, 12, 'bold'),yscrollcommand=scrollbar.set)
        self.CustomerList.bind('<<ListboxSelect>>', self.__getCustomer)
        self.CustomerList.grid(row=0, column=0, padx=8)
        scrollbar.config(command=self.CustomerList.yview)

        buttonCreateTable = Button(ButtonFrame, text="Add New", font=(config.font, 20, 'bold'), height=1, width=10, bd=4, command=self.addDataCustomer)
        buttonCreateTable.grid(row=0, column = 0)

        # self.btnDisplayData = Button(ButtonFrame, text="Display", font=(config.font, 20, 'bold'), height=1, width=10, bd=4, command=DisplayData)
        # self.btnDisplayData.grid(row=0, column=1)

        buttonClearData = Button(ButtonFrame, text="Clear", font=(config.font, 20, 'bold'), height=1, width=10, bd=4,command=self.clearData)
        buttonClearData.grid(row=0, column=1)

        # self.btnSearchData = Button(ButtonFrame, text="Search", font=(config.font, 20, 'bold'), height=1, width=10, bd=4,command=searchDatabase)
        # self.btnSearchData.grid(row=0, column=4)

        buttonUpdateData = Button(ButtonFrame, text="Update", font=(config.font, 20, 'bold'), height=1, width=10, bd=4,command=self.updateCustomer)
        buttonUpdateData.grid(row=0, column=2)

        buttonExit = Button(ButtonFrame, text="Exit", font=(config.font, 20, 'bold'), height=1, width=10, bd=4, command=self.exit)
        buttonExit.grid(row=0, column=3)

        btnDeleteData = Button(ButtonFrame, text="Delete", font=(config.font, 20, 'bold'), height=1, width=10, bd=4,command=self.deleteDatabase)
        btnDeleteData.grid(row=0, column=9)

        notebook.add(DataFrame, text="Customer")


    # TODO: Добавить такие же функции для остальных таблиц
    def __getSeller(self, event):
        searchSeller = self.SellerList.curselection()
        if not searchSeller:
            return
        
        seller = self.SellerList.get(searchSeller[0])

        # Обновление в полях ввода
        self.textSellerID.delete(0, END)
        self.textSellerID.insert(END, seller[0])
        self.textSellerFullName.delete(0, END)
        self.textSellerFullName.insert(END, seller[1])
        self.textSellerPhoneNumber.delete(0, END)
        self.textSellerPhoneNumber.insert(END, seller[2])

    def __getCustomer(self, event):
        search = self.CustomerList.curselection()
        if not search:
            return
        
        customer = self.CustomerList.get(search[0])

        # Обновление в полях ввода
        self.textCustomerID.delete(0, END)
        self.textCustomerID.insert(END, customer[0])
        self.textCustomerFullName.delete(0, END)
        self.textCustomerFullName.insert(END, customer[1])
        self.textCustomerPhoneNumber.delete(0, END)
        self.textCustomerPhoneNumber.insert(END, customer[2])
