import sqlite3


def authenticate(uname,pword):
    connection = sqlite3.connect("login.db")
    c = connection.cursor()
    ans = c.execute('SELECT * FROM logins where username = "' + uname + '" and password = "' + pword + '";')
    for r in ans:
        return True
    return False

def create_user(uname,pword):
    connection = sqlite3.connect("login.db")
    c = connection.cursor()
    ans = c.execute('SELECT * FROM logins where username = "' + uname + '";')
    for r in ans:
        return False
    ans = c.execute('INSERT INTO logins values("' + uname + '", "' + pword + '");')
    connection.commit()
    return True

        
#create_user("asdf@gmail.com", "asdfasdf")
