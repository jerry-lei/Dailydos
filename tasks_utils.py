import sqlite3

def get_full_sql(user):
	conn = sqlite3.connect("tasks.db")
	c = conn.cursor()
        temp = []
	for row in c.execute('SELECT * FROM tasks where email = "' + user + '";'):
                temp.append(row)
        conn.close()
        return temp

def get_tasks(user):
        temp = get_full_sql(user)
        i = 0
        temp2 = []
        while(i < len(temp)):
                temp2.append(temp[i][1])
                i+=1
        return temp2

#print get_tasks("jerrylei98@gmail.com")
