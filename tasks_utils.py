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

def remove_tasks(task_list):
        if len(task_list) > 0:
                conn = sqlite3.connect("tasks.db")
                c = conn.cursor()
                for item in task_list: 
                        c.execute('DELETE FROM tasks WHERE task="' + item + '";')
                conn.commit()
                conn.close()
                

def clear_tasks(user):
        conn = sqlite3.connect("tasks.db")
        c = conn.cursor()
        c.execute('DELETE FROM tasks WHERE email="' + user + '";')
        conn.commit()
        conn.close()                              

#temp = ['cheese', 'try 3', 'try again 217']
#remove_tasks(temp)

#print get_tasks("jerrylei98@gmail.com")
