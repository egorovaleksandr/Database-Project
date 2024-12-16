#frontend
from tkinter import *
from tkinter.messagebox import showinfo, askyesno
from tkinter import Frame
import backendDB
import config

class Frontend:
    def __init__(self, window):
        self.window = window
        self.__setupWindow()

        self.databaseCreated = False

        self
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

    def __setupVariables(self):
        self.SellerID = IntVar()
        self.SellerFullName = StringVar()
        self.SellerFullNumber = StringVar()

    def __setupFrame(self):
        mainFrame = Frame(self.window, bg=config.background)
        mainFrame.grid()
        titleFrame = Frame(mainFrame, bd=2, padx=54,pady=8, bg=config.text_background, relief=RIDGE)
        titleFrame.pack(side=TOP)
        labelTitle = Label(titleFrame, font=(config.font, 48, 'bold'), text="Car Dealership Database", bg=config.text_background)
        labelTitle.grid()
        ButtonFrame = Frame(mainFrame, bd=2, width=1350, height=70, padx=19, pady=10, bg=config.text_background, relief=RIDGE)
        ButtonFrame.pack(side=BOTTOM)
        DataFrame = Frame(mainFrame, bd=1, width=1300, height=400, padx=20, pady=20, relief=RIDGE,bg=config.background)
        DataFrame.pack(side=BOTTOM)
        DataFrameLEFT = LabelFrame(DataFrame, bd=1, width=1000, height=600, padx=20, relief=RIDGE, bg=config.text_background, font=(config.font, 26, 'bold'), text="Customer Info\n")
        DataFrameLEFT.pack(side=LEFT)
        DataFrameRIGHT = LabelFrame(DataFrame, bd=1, width=450, height=300, padx=31, pady=3, relief=RIDGE,bg=config.text_background,font=(config.font, 20, 'bold'),text="Customer Data\n")
        DataFrameRIGHT.pack(side=RIGHT)

        # Seller

        self.labelSellerID = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Seller's ID:",padx=2,pady=2,bg="Ghost White")
        self.labelSellerID.grid(row=0,column=0,sticky=W)
        self.textSellerID = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=self.SellerID, width=39)
        self.textSellerID.grid(row=0, column=1)

        self.labelSellerFullName = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Full Name:", padx=2, pady=2,bg="Ghost White")
        self.labelSellerFullName.grid(row=1, column=0, sticky=W)
        self.textSellerFullName = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=self.SellerFullName, width=39)
        self.textSellerFullName.grid(row=1, column=1)

        self.labelSellerPhoneNumber = Label(DataFrameLEFT, font=('times new roman', 20, 'bold'), text="Phone Number", padx=2, pady=2,bg="Ghost White")
        self.labelSellerPhoneNumber.grid(row=2, column=0, sticky=W)
        self.textSellerPhoneNumber = Entry(DataFrameLEFT, font=('times new roman', 20, 'bold'), textvariable=self.SellerFullNumber, width=39)
        self.textSellerPhoneNumber.grid(row=2, column=1)

#--------------------------------------scroll bar and list box----------------------------------------------------------------------------
        scrollbar= Scrollbar(DataFrameRIGHT)
        scrollbar.grid(row=0,column=1,sticky='ns')

        self.SellerList = Listbox(DataFrameRIGHT, width=41, height=16, font=('times new roman', 12, 'bold'),yscrollcommand=scrollbar.set)
        self.SellerList.bind('<<ListboxSelect>>', self.__getSeller())
        self.SellerList.grid(row=0, column=0, padx=8)
        scrollbar.config(command=self.SellerList.yview)

    def __getSeller(self):
        searchSeller = self.SellerList.curselection()[0]
        sd = self.SellerList.get(searchSeller)

        self.textSellerID.delete(0, END)
        self.textSellerID.insert(END, sd[1])
        self.textSellerFullName.delete(0, END)
        self.textSellerFullName.insert(END, sd[2])
        self.textSellerPhoneNumber.delete(0, END)
        self.textSellerPhoneNumber.insert(END, sd[3])