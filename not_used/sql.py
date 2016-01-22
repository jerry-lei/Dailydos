import sqlite3

with sqlite3.connect("login.db") as connection:
    c = connection.cursor()
    c.execute("CREATE TABLE logins(username TEXT, password TEXT)")
