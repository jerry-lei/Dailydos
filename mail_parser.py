#import smtplib, email
import sqlite3

connection = sqlite3.connect("tasks.db")
c = connection.cursor()
ans = c.execute('INSERT INTO tasks values("queenjerry@live.com", "homework", 0)')
connection.commit()
