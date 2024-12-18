import sqlite3

datapath = 'databases\dealership.db'
ddl_create = 'dealershipDB\ddl_create.sql'
ddl_drop = 'dealershipDB\ddl_drop.sql'

def checkTableNotExists(table_name):
    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            (table_name,)
            )
        rows = cursor.fetchone()
    return not rows

#methods for DDL
def createDealershipDB():
    try:
        with sqlite3.connect(datapath) as connection:
            cursor = connection.cursor()
            with open(ddl_create, 'r') as f:
                sql_script = f.read()
            cursor.executescript(sql_script)
            connection.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при создании базы данных: {e}")

def dropDealershipDB():
    try:
        with sqlite3.connect(datapath) as connection:
            cursor = connection.cursor()
            with open(ddl_drop, 'r') as f:
                sql_script = f.read()
            cursor.executescript(sql_script)
            connection.commit()
    except sqlite3.Error as e:
        print(f"Ошибка при удалении базы данных: {e}")

#methods for DML (inserts)
def addDataCustomer(full_name, phone_number):
    if checkTableNotExists("customer"):
        createDealershipDB()
    
    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO customer (full_name, phone_number) VALUES (?, ?)",
            (full_name, phone_number)
            )
        connection.commit()


def addDataSeller(full_name, phone_number):
    if checkTableNotExists("seller"):
        createDealershipDB()
    
    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO seller (full_name, phone_number) VALUES (?, ?)",
            (full_name, phone_number)
            )
        connection.commit()

def addDataMaker(country, company):
    if checkTableNotExists("maker"):
        createDealershipDB()
    
    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO maker (country, company) VALUES (?, ?)",
            (country, company)
            )
        connection.commit()

def addDataModel(model_name, color, number_of_seats, engine):
    if checkTableNotExists("model"):
        createDealershipDB()
    
    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO model (model_name, color, number_of_seats, engine) VALUES (?, ?, ?, ?)",
            (model_name, color, number_of_seats, engine)
            )
        connection.commit()

def addDataPrice(price, date_from, date_to):
    if checkTableNotExists("price"):
        createDealershipDB()
    
    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO price (price, date_from, date_to) VALUES (?, ?, ?)",
            (price, date_from, date_to)
            )
        connection.commit()

def addDataAutomobile(car_brand, maker_id, model_id):
    if checkTableNotExists("automobile"):
        createDealershipDB()
    
    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO automobile (car_brand, maker_id, model_id) VALUES (?, ?, ?)",
            (car_brand, maker_id, model_id)
            )
        connection.commit()

def addDataPayment(pay_method, pay_date, account_number, receipt_size):
    if checkTableNotExists("payment"):
        createDealershipDB()
    
    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO payment (pay_method, pay_date, account_number, receipt_size) VALUES (?, ?, ?, ?)",
            (pay_method, pay_date, account_number, receipt_size)
            )
        connection.commit()

def addDataServiceInfo(seller_id, automobile_id, service_date, pay_id):
    if checkTableNotExists("service_info"):
        createDealershipDB()
    
    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO service_info (seller_id, automobile_id, service_date, pay_id) VALUES (?, ?, ?, ?)",
            (seller_id, automobile_id, service_date, pay_id)
            )
        connection.commit()

def addDataService(customer_id, service_id, automobile_id):
    if checkTableNotExists("service"):
        createDealershipDB()
    
    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO service (customer_id, service_id, automobile_id) VALUES (?, ?, ?)",
            (customer_id, service_id, automobile_id)
            )
        connection.commit()

#methods for DML (selects)
def viewData(table_name):
    if checkTableNotExists(table_name):
        createDealershipDB()
    
    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM " + table_name)
        rows = cursor.fetchall()
    return rows