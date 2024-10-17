import sqlite3

connection = sqlite3.connect('crud_functions2.db')  # подключаемся к файлу с базой данных
cursor = connection.cursor()  # создаем объект курсора

# Создание таблицы. Задаем параметры(название графы и тип данных)


def initiate_db():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT NOT NULL,
price INTEGER NOT NULL
)
''')
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER NOT NULL,
balance INTEGER NOT NULL
)
''')


connection.commit()  # save state

initiate_db()


cursor.execute("DELETE FROM Products")
for num in range(1, 5):
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
                   (f"Продукт {num}", f"Описание {num}", num * 100))
connection.commit()


def add_user(username, email, age):
    cursor.execute('INSERT INTO Users (username,email,age ,balance) VALUES (?,?,?,1000)', (username,
                                                                                           email, age))
    connection.commit()


def is_included(username):
    cursor.execute("SELECT * FROM Users")
    users = cursor.fetchall()
    for user in users:
        if username == user[1]:
            return True
    return False


def get_all_products():
    cursor.execute('''SELECT * FROM Products''')
    return cursor.fetchall()
