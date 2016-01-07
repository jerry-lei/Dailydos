from pymongo import MongoClient
import re
#need to switch to mongo for server-sided scripts
#use string.isalnum() checks for alphanumeric and spaces

connection = MongoClient()
database = connection['database']

def clean(text):
    return re.sub(r'\W+', '', text)

def if_all_alphanumeric(username, password):
    if !username.isalnum():
        return False
    if !password.isalnum():
        return False
    return True

def authenticate(username, password):
    """
    Parameters: Username, Password
    Checks db if username matches password
    Returns list of codes located in error_code_list, empty list if all conditions met
    """
    connection = MongoClient()
    cursor = database.logins.find({'username': username, 'password':password})
    for r in cursor:
        return True
    return False
    connection.close()

def create_user(username, password):
    """
    Parameters: Username, Password
    Checks db if username exists. Puts username and password into db.
    Returns list of codes located in error_code_list, empty list if all conditions met
    """
    ans = database.logins.find({username:True})
    for r in ans:
        return False
    d = {'username': username, 'password': password}
    database.logins.insert(d)
    connection = MongoClient()
    db = connection['logins']
    ans = db.logins.find({'username': username}).count()
    if check != 0:
        return False
    return True
    connection.close()
    
