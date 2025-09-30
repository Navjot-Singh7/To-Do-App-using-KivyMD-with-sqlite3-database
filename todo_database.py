import sqlite3
	
def create_database():
	conn = sqlite3.connect("todo.db")
	c = conn.cursor()
		
	c.execute("""CREATE TABLE if not exists Tasks(
		 task_name TEXT,
		 task_done TEXT) """)
		
	conn.commit()
	conn.close()
	
def add_task(task_name , task_done):
	conn = sqlite3.connect("todo.db")
	c = conn.cursor()
	
	c.execute("""INSERT INTO Tasks VALUES (?, ?) """, (task_name, task_done))
		
	conn.commit()
	conn.close()



def get_tasks():
	conn = sqlite3.connect("todo.db")
	c = conn.cursor()
	
	c.execute("""SELECT * FROM Tasks """)
	
	return c.fetchall()

#print(get_tasks())

def delete_tasks(task_name):
	conn = sqlite3.connect("todo.db")
	c = conn.cursor()
	
	c.execute("""DELETE FROM Tasks WHERE task_name = ?  """, (task_name,))
	conn.commit()
	conn.close()

#delete_tasks()

def mark_task_as_complete(task_name):
	conn = sqlite3.connect("todo.db")
	c = conn.cursor()
	
	c.execute("""UPDATE Tasks SET task_done="1" WHERE task_name = ? """, (task_name,))
	conn.commit()
	conn.close()

#mark_task_as_complete()
	
def mark_task_as_incomplete(task_name):
	conn = sqlite3.connect("todo.db")
	c = conn.cursor()
	
	c.execute("""UPDATE Tasks SET task_done="0" WHERE task_name = ? """, (task_name,))
	conn.commit()
	conn.close()

#mark_task_as_incomplete()