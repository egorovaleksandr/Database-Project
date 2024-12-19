"""
Implements methods for working with the database
"""

import sqlite3
import os
import config

current_dir = os.path.dirname(__file__)
base_dir = os.path.abspath(os.path.join(current_dir, '..'))
datapath = os.path.join(base_dir, 'databases', 'dealership.db')
ddl_create = os.path.join(base_dir, 'sqlite_scripts', 'ddl_create.sql')
ddl_drop = os.path.join(base_dir, 'sqlite_scripts', 'ddl_drop.sql')
dml_inserts = os.path.join(base_dir, 'sqlite_scripts', 'dml_inserts.sql')
dml_deletes = os.path.join(base_dir, 'sqlite_scripts', 'dml_deletes.sql')

def check_table_not_exists(table_name):
    """
    Checks for the existence of a table
    """
    if table_name not in config.tables:
        print("Неверно указано имя таблицы: " + table_name)

    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "SELECT name FROM sqlite_master WHERE type='table' AND name=?",
            (table_name,)
            )
        rows = cursor.fetchone()
    return not rows

#methods for DDL
def create_dealership_db():
    """
    Creates a dealership database
    """
    try:
        with sqlite3.connect(datapath) as connection:
            cursor = connection.cursor()
            with open(ddl_create, 'r', encoding='utf-8') as file:
                sql_script = file.read()
            cursor.executescript(sql_script)
            connection.commit()
    except sqlite3.Error as error:
        print(f"Ошибка при создании базы данных: {error}")

def drop_dealership_db():
    """
    Deletes the database
    """
    try:
        with sqlite3.connect(datapath) as connection:
            cursor = connection.cursor()
            with open(ddl_drop, 'r', encoding='utf-8') as file:
                sql_script = file.read()
            cursor.executescript(sql_script)
            connection.commit()
    except sqlite3.Error as error:
        print(f"Ошибка при удалении базы данных: {error}")

#methods for DML (inserts)
def clear_database():
    """
    Clears all tables in the database if they exists
    """
    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        with open(dml_deletes, 'r', encoding='utf-8') as file:
            sql_script = file.read()
        cursor.executescript(sql_script)
        connection.commit()

def test_filling():
    """
    Fills the database with test data
    """
    try:
        with sqlite3.connect(datapath) as connection:
            cursor = connection.cursor()
            with open(dml_inserts, 'r', encoding='utf-8') as file:
                sql_script = file.read()
            cursor.executescript(sql_script)
            connection.commit()
    except sqlite3.Error as error:
        print(f"Ошибка при тестовом заполнении базы данных: {error}")


def add_data_customer(full_name, phone_number):
    """
    Adds data to the table customer
    """
    if check_table_not_exists("customer"):
        create_dealership_db()

    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO customer (full_name, phone_number) VALUES (?, ?)",
                (full_name, phone_number)
                )
            connection.commit()
        except sqlite3.Error as error:
            print(f"Ошибка при добавлении данных: {error}")


def add_data_seller(full_name, phone_number):
    """
    Adds data to the table seller
    """
    if check_table_not_exists("seller"):
        create_dealership_db()

    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        try:
            cursor.execute(
                "INSERT INTO seller (full_name, phone_number) VALUES (?, ?)",
                (full_name, phone_number)
                )
            connection.commit()
        except sqlite3.Error as error:
            print(f"Ошибка при добавлении данных: {error}")

def add_data_maker(country, company):
    """
    Adds data to the table maker
    """
    if check_table_not_exists("maker"):
        create_dealership_db()

    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO maker (country, company) VALUES (?, ?)",
            (country, company)
            )
        connection.commit()

def add_data_model(model_name, color, number_of_seats, engine):
    """
    Adds data to the table model
    """
    if check_table_not_exists("model"):
        create_dealership_db()

    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO model (model_name, color, number_of_seats, engine) VALUES (?, ?, ?, ?)",
            (model_name, color, number_of_seats, engine)
            )
        connection.commit()

def add_data_price(price, date_from, date_to):
    """
    Adds data to the table price
    """
    if check_table_not_exists("price"):
        create_dealership_db()

    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO price (price, date_from, date_to) VALUES (?, ?, ?)",
            (price, date_from, date_to)
            )
        connection.commit()

def add_data_automobile(car_brand, maker_id, model_id):
    """
    Adds data to the table automobile
    """
    if check_table_not_exists("automobile"):
        create_dealership_db()

    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO automobile (car_brand, maker_id, model_id) VALUES (?, ?, ?)",
            (car_brand, maker_id, model_id)
            )
        connection.commit()

def add_data_payment(pay_method, pay_date, account_number, receipt_size):
    """
    Adds data to the table payment
    """
    if check_table_not_exists("payment"):
        create_dealership_db()

    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            '''INSERT INTO payment
            (pay_method, pay_date, account_number, receipt_size) VALUES (?, ?, ?, ?)''',
            (pay_method, pay_date, account_number, receipt_size)
            )
        connection.commit()

def add_data_service_info(seller_id, automobile_id, service_date, pay_id):
    """
    Adds data to the table service_info
    """
    if check_table_not_exists("service_info"):
        create_dealership_db()

    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            '''INSERT INTO service_info
            (seller_id, automobile_id, service_date, pay_id) VALUES (?, ?, ?, ?)''',
            (seller_id, automobile_id, service_date, pay_id)
            )
        connection.commit()

def add_data_service(customer_id, service_id, automobile_id):
    """
    Adds data to the table service
    """
    if check_table_not_exists("service"):
        create_dealership_db()

    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute(
            "INSERT INTO service (customer_id, service_id, automobile_id) VALUES (?, ?, ?)",
            (customer_id, service_id, automobile_id)
            )
        connection.commit()

#methods for DML (selects)
def view_data(table_name):
    """
    Selects all rows from the table
    """
    if table_name not in config.tables:
        print("Неверно указано имя таблицы: " + table_name)

    if check_table_not_exists(table_name):
        create_dealership_db()

    with sqlite3.connect(datapath) as connection:
        cursor = connection.cursor()
        cursor.execute("SELECT * FROM " + table_name)
        rows = cursor.fetchall()
    return rows
