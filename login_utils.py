import sqlite3
import re

def authenticate(username,password):
    uname = username
    conn = sqlite3.connect("../login.db")
    #second connection for file settings
    c = conn.cursor()



