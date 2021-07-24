import sqlite3 as sql

con=sql.connect('New PY/database/userbd.db')
cur=con.cursor()

list_table=cur.execute("SELECT name FROM sqlite_master WHERE type='table' and name <> 'sqlite_sequence';").fetchall()
for row in list_table:
    print("DROP TABLE IF  EXISTS "+row[0])
    cur.execute("DROP TABLE IF  EXISTS "+row[0])

cur.execute('''CREATE TABLE alert_type (
	id	INTEGER NOT NULL,
	name TEXT,
    desc TEXT,
	PRIMARY KEY(id AUTOINCREMENT)
)''')

cur.execute('''CREATE TABLE alert (
	id	INTEGER NOT NULL,
	Name TEXT,
	Type INTEGER,
	FOREIGN KEY(Type) REFERENCES alert_type(id) ON DELETE RESTRICT,
	PRIMARY KEY(id AUTOINCREMENT)
)''')

 

con.commit()
con.close()