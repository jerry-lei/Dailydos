import sqlite3
import re
#need to switch to mongo for server-sided scripts
#use string.isalnum() checks for alphanumeric and spaces

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
    Parameters: Username


    """
    if if_all_alphanumeric(username,password):
        ##
        ##
        
    return False

def create_user(username, password):
    uname = username
    pword = password

