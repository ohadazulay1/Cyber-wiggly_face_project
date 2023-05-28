import sqlite3

connection = sqlite3.connect('database.db')
cursor = connection.cursor()
cursor.execute("""CREATE TABLE users(
        username text not null,
        password text not null,
        highScore real not null
    )""")
connection.commit()
connection.close()

