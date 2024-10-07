import sqlite3

connection = sqlite3.connect('not_telegram.db')
cursor = connection.cursor() # создаем объект курсора

# Создание таблицы. Задаем параметры.
cursor.execute('''
CREATE TABLE IF NOT EXISTS Users(
id INTEGER PRIMARY KEY,
username TEXT NOT NULL,
email TEXT NOT NULL,
age INTEGER,
balance INTEGER NOT NULL
)
''')
# cursor.execute('CREATE INDEX IF NOT EXISTS idx_email on Users(email)')
# for i in range(1,11):
#     cursor.execute('INSERT INTO Users (username,email,age ,balance) VALUES (?,?,?,?)',
#                    ((f'User{i}',f' example{i}@gmail.com',f'{i * 10}', '1000')))
#
# for k in range (1,11,2):
#     cursor.execute('UPDATE Users SET balance = ? WHERE id = ?',(500,k))  # изменение параметров таблицы
# for j in range (1,11,3):
#     cursor.execute('DELETE FROM Users WHERE id = ? ',(j,))
cursor.execute('SELECT username,age,balance, email FROM Users WHERE age != ?', (60,)) # считываем определенную информацию с базы данных
users = cursor.fetchall()
for user in users:
    print(f'Имя: {user[0]} | Почта: {user[3]}| Возраст: {user[1]}| Баланс: {user[2]}')



connection.commit() # save state
connection.close()  # save