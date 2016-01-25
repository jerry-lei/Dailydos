import sqlite3

def getPosts():
	conn = sqlite3.connect("posts.db")
	c = conn.cursor()
	posts = c.execute("SELECT DISTINCT * FROM logins ORDER BY postsList.postNum DESC")
	conn.commit()
	return posts
	conn.close()