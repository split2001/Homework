import sqlite3


connection = sqlite3.connect('crud_functions.db')  # подключаемся к файлу с базой данных
cursor = connection.cursor()  # создаем объект курсора


# Создание таблицы. Задаем параметры(название графы и тип данных)
cursor.execute("DELETE FROM Products")
for num in range(1, 5):
    cursor.execute("INSERT INTO Products (title, description, price) VALUES (?, ?, ?)",
               (f"Продукт {num}", f"Описание {num}", num * 100))
connection.commit()




def initiate_db():
    cursor.execute('''
CREATE TABLE IF NOT EXISTS Products(
id INTEGER PRIMARY KEY,
title TEXT NOT NULL,
description TEXT NOT NULL,
price INTEGER NOT NULL
)
''')
    connection.commit()   # save state


def get_all_products():
    cursor.execute('''SELECT * FROM Products''')
    return cursor.fetchall()




