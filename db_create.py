import sqlite3
from _config import DATABASE_PATH

conn=sqlite3.connect(DATABASE_PATH)

c = conn.cursor()
#c.execute("CREATE TABLE tasks(task_id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, due_date TEXT NOT NULL, priority INTEGER NOT NULL, status INTEGER NOT NULL)")
    
c.execute("INSERT INTO tasks (name, due_date, priority, status) VALUES ('Finish this tutorial', '03/25/2015', 10, 1)")
c.execute("INSERT INTO tasks (name, due_date, priority, status) VALUES ('Finish Real Python Course 2', '03/28/2015', 10, 1)")
    
conn.commit()
conn.close()