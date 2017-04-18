import sqlite3
conn = sqlite3.connect('db_rank_test.db')
c = conn.cursor()

def create_table(table_definition):

	try:
		c.execute('CREATE TABLE ?' % table_definition)
	except:
		print("Table exits!")
		c.execute('DELETE FROM books')
		print("Table has been deleted!")
	finally:
		print("Table created successfully!")

create_table('books (name TEXT, ctime TEXT, crank TEXT)')

stu_info = [
	('leiyunhe','2010-1-2T0080',None),
	('fengruibo','2010-1-3T0080',None),
	('crane','2010-1-1T0080',None),
]

c.executemany('INSERT INTO books VALUES (?,?,?)', stu_info)
try:
	for row in c.execute('SELECT * FROM books ORDER BY ctime'):
		print(row)
		c.execute('UPDATE ')
except:
	pass
finally:
	conn.commit()


# return Max and Min value
c.execute('SELECT MAX(ctime) FROM books')
print(c.fetchone())

c.execute('SELECT MIN(ctime) FROM books')
min_value = c.fetchone()
print(min_value)


# return Max and Min item
c.execute('SELECT * FROM books WHERE ctime =(SELECT MAX(ctime) FROM books) ')
print(c.fetchone())

c.execute('SELECT * FROM books WHERE ctime =(SELECT MIN(ctime) FROM books) ')
print(c.fetchone())



conn.close()




