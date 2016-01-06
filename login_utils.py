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

def error_code_list():
    return """
    Parameter: authenticate, create_user, change password, 
    If code_list contains: 
    001 >>  username and password matches, no return
    002 >>  username and password does not match
    003 >>  username is not alphanumeric
    004 >>  password is not alphanumeric
    005 >>  username is already taken
    """        


def authenticate(username, password):
    """
    Parameters: Username, Password
    Checks db if username matches password
    Returns list of codes located in error_code_list, empty list if all conditions met
    """
    error_codes = [] #add to using error_codes.append(int)
    if if_all_alphanumeric(username,password):
        ##
        ##
        
    return False

def create_user(username, password):
    """
    Parameters: Username, Password
    Checks db if username exists. Puts username and password into db.
    Returns list of codes located in error_code_list, empty list if all conditions met
    """
    error_codes = [] #add to using error_codes.append(int)
    uname = username
    pword = password
    
