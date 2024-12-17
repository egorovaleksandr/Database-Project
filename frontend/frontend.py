#frontend
from tkinter import *
from tkinter.messagebox import showinfo, askyesno
from tkinter.ttk import Notebook
import backendDB
import config


def numberFieldValid(value):
    if value == "":
        return True
    try:
        int(value)
        return True
    except ValueError:
        return False

class Frontend:
    def __init__(self, window):
        self.window = window
        self.__setupWindow()

        self.databaseCreated = False

        self.__setupVariables()
        self.__setupFrame()


    def exit(self):
        exiting = askyesno(config.title, "Confirm if you want to exit")
        if exiting:
            self.window.destroy()
        
    def createNewDatabase(self):
        if self.databaseCreated:
            creating = askyesno(config.title, "Are you sure you want to recreate database?\n The old one will be deleted!")
        else: 
            creating = True
        if creating:
            backendDB.dropDealershipDB()
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

    def __setupFrame(self):
        mainFrame = Frame(self.window, bg=config.background)
        mainFrame.grid()
        # titleFrame = Frame(mainFrame, bd=2, padx=54,pady=8, bg=config.text_background, relief=RIDGE)
        # titleFrame.pack(side=TOP)
        # labelTitle = Label(titleFrame, font=(config.font, 48, 'bold'), text="Car Dealership Database", bg=config.text_background)
        # labelTitle.grid()
        ButtonFrame = Frame(mainFrame, bd=2, width=1350, height=70, padx=19, pady=10, bg=config.text_background, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)

        
        notebook = Notebook(mainFrame)
        notebook.pack(expand=True, fill=BOTH)

        DataFrames = []
        DataFramesLEFT = []
        DataFramesRIGHT = []

        # tablesInfo = ...

        for i in range(3):
            newDataFrame = Frame(notebook, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE,bg=config.background)
            # newDataFrameLEFT = ...
            # newDataFrameRIGHT = ...

            #DataFrames.append(newDataFrame)
            #DataFramesLEFT.append(newDataFrameLEFT)
            #DataFramesRIGHT.append(newDataFrameRIGHT)


        # TODO: Выше сделать цикл по аналогии с тем, что ниже
        DataFrame = Frame(mainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE,bg=config.background)
        DataFrame.pack(side=BOTTOM)

        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg=config.text_background, font=(config.font, 26, 'bold'), text="Table Info\n")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,bg=config.text_background,font=(config.font, 20, 'bold'),text="Table Data\n")
        DataFrameRIGHT.pack(side=RIGHT)

        vcmd = (self.window.register(numberFieldValid))

        # Seller

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
        self.textSellerPhoneNumber = Entry(DataFrameLEFT, font=(config.font, 20, 'bold'), textvariable=self.SellerPhoneNumber, width=39)
        self.textSellerPhoneNumber.grid(row=2, column=1)

        scrollbar= Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        self.SellerList = Listbox(DataFrameRIGHT, width=41, height=16, font=(config.font, 12, 'bold'),yscrollcommand=scrollbar.set)
        self.SellerList.bind('<<ListboxSelect>>', self.__getSeller)
        self.SellerList.grid(row=0, column=0, padx=8)
        scrollbar.config(command=self.SellerList.yview)

    # TODO: Добавить такие же функции для остальных таблиц
    def __getSeller(self, event):
        searchSeller = self.SellerList.curselection()
        if not searchSeller:
            return
        
        seller = self.SellerList.get(searchSeller[0])

        # Обновление в полях ввода
        self.textSellerID.delete(0, END)
        self.textSellerID.insert(END, seller[1])
        self.textSellerFullName.delete(0, END)
        self.textSellerFullName.insert(END, seller[2])
        self.textSellerPhoneNumber.delete(0, END)
        self.textSellerPhoneNumber.insert(END, seller[3])

