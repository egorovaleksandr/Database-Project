import sqlite3
import commands

datapath = 'dealership.db'

#methods for DDL
def createDealershipDB():
    connection = sqlite3.connect(datapath)
    cursor = connection.cursor()
    cursor.executescript(commands.DDLCommands.createDB_command)
    connection.commit()
    connection.close()

def dropDealershipDB():
    connection = sqlite3.connect(datapath)
    cursor = connection.cursor()
    cursor.executescript(commands.DDLCommands.dropDB_command)
    connection.commit()
    connection.close()

#methods for DML (inserts)
def addDataCustomer(customer_id, full_name, phone_number):
    connection = sqlite3.connect(datapath)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO customer (customer_id, full_name, phone_number) VALUES (?, ?, ?)", (customer_id, full_name, phone_number))
    connection.commit()
    connection.close()

def addDataSeller(seller_id, full_name, phone_number):
    connection = sqlite3.connect(datapath)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO seller (seller_id, full_name, phone_number) VALUES (?, ?, ?)", (seller_id, full_name, phone_number))
    connection.commit()
    connection.close()

def addDataMaker(maker_id, country, company):
    connection = sqlite3.connect(datapath)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO maker (maker_id, country, company) VALUES (?, ?, ?)", (maker_id, country, company))
    connection.commit()
    connection.close()

def addDataModel(model_id, model_name, color, number_of_seats, engine):
    connection = sqlite3.connect(datapath)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO model (model_id, model_name, color, number_of_seats, engine) VALUES (?, ?, ?, ?, ?)", (model_id, model_name, color, number_of_seats, engine))
    connection.commit()
    connection.close()

def addDataPrice(model_id, price, date_from, date_to):
    connection = sqlite3.connect(datapath)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO price (model_id, price, date_from, date_to) VALUES (?, ?, ?, ?)", (model_id, price, date_from, date_to))
    connection.commit()
    connection.close()

def addDataAutomobile(automobile_id, car_brand, maker_id, model_id):
    connection = sqlite3.connect(datapath)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO automobile (automobile_id, car_brand, maker_id, model_id) VALUES (?, ?, ?, ?)", (automobile_id, car_brand, maker_id, model_id))
    connection.commit()
    connection.close()

def addDataPayment(pay_id, pay_method, pay_date, account_number, receipt_size):
    connection = sqlite3.connect(datapath)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO payment (pay_id, pay_method, pay_date, account_number, receipt_size) VALUES (?, ?, ?, ?, ?)", (pay_id, pay_method, pay_date, account_number, receipt_size))
    connection.commit()
    connection.close()

def addDataServiceInfo(service_id, seller_id, automobile_id, service_date, pay_id):
    connection = sqlite3.connect(datapath)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO service_info (service_id, seller_id, automobile_id, service_date, pay_id) VALUES (?, ?, ?, ?, ?)", (service_id, seller_id, automobile_id, service_date, pay_id))
    connection.commit()
    connection.close()

def addDataService(customer_id, service_id, automobile_id):
    connection = sqlite3.connect(datapath)
    cursor = connection.cursor()
    cursor.execute("INSERT INTO service (customer_id, service_id, automobile_id) VALUES (?, ?, ?)", (customer_id, service_id, automobile_id))
    connection.commit()
    connection.close()

#methods for DML (selects)
def viewData(table_name):
    connection = sqlite3.connect(datapath)
    cursor = connection.cursor()
    cursor.execute(f"SELECT * FROM " + table_name)
    rows = cursor.fetchall()
    connection.close()
    return rows