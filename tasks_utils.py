import sqlite3

def getPosts(user):
	conn = sqlite3.connect("posts.db")
	c = conn.cursor()
	posts = c.execute('SELECT * FROM tasks where tasks.email = "' + user + '";')
	conn.commit()
	return posts
	conn.close()