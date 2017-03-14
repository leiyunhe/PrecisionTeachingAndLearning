import sqlite3

conn = sqlite3.connect('database.db')
print("Opened database successfully")

# conn.execute('CREATE TABLE qw (qttime TEXT, city_name TEXT, weather TEXT, temperature TEXT)')
conn.execute('CREATE TABLE submit_issue (github_user_name TEXT, chap1_time TEXT, chap2_time TEXT, chap3_time TEXT, chap4_time TEXT, chap5_time TEXT, chap7_time TEXT)')
print("Table created successfully")
conn.close()