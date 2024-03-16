# ЗАДАНИЕ 
# Выберете минимум 1 любую БД и напиши функции(описаны требования у каждой бд) для работы с БД через CLI(командный интерфейс строки(через консоль)) в питоне при помощи sqlite3
# Создать  БД “онлайн-магазина,”с таблицами users, orders, products(таблицы можно создать и не через питон) и требования:
# Пользователи могут регистрироваться, входить в систему и изменять свои данные.
# Администратор может добавлять, удалять и изменять информацию о продуктах.
# Пользователи могут просматривать каталог товаров, добавлять их в корзину и оформлять заказы.
# После оформления заказа пользователь должен получить подтверждение по электронной почте.
# Статус заказа должен автоматически изменяться в зависимости от его выполнения (например, "в обработке", "отправлен", "доставлен").

import sqlite3

def connect_to_database():
    conn = sqlite3.connect('online_store.db')
    return conn, conn.cursor()

def register_user(username, password, email):
    conn, cursor = connect_to_database()
    cursor.execute("INSERT INTO users (username, password, email) VALUES (?, ?, ?)", (username, password, email))
    conn.commit()
    conn.close()

def login(username, password):
    conn, cursor = connect_to_database()
    cursor.execute("SELECT * FROM users WHERE username=? AND password=?", (username, password))
    user = cursor.fetchone()
    conn.close()
    return user

def create_users_table():
    conn, cursor = connect_to_database()
    cursor.execute('''
        CREATE TABLE IF NOT EXISTS users (
            id INTEGER PRIMARY KEY,
            username TEXT,
            password TEXT,
            email TEXT
        )
    ''')
    conn.commit()
    conn.close()

create_users_table()

register_user("user1", "password1", "user1@example.com")

user = login("user1", "password1")
if user:
    print("Вход выполнен успешно")
else:
    print("Неверные учетные данные")
