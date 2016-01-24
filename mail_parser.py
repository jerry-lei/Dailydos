#import smtplib, email
import sqlite3
import os
from email.parser import Parser

if os.path.getsize("/var/mail/group") > 0:
    headers = Parser().parse(open("/var/mail/group"))
    
    connection = sqlite3.connect("tasks.db")
    c = connection.cursor()
    from_email = headers['from']
    from_email = from_email[from_email.find("<")+1:from_email.find(">")]
    ans = c.execute('INSERT INTO tasks values("' + from_email + '", "' + headers['subject'] + '", 0)')
    connection.commit()


