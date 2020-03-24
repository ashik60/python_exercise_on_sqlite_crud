import sqlite3
conn = sqlite3.connect('01_author.sqlite')
cur = conn.cursor();

# create table
cur.execute('''CREATE TABLE author\
(id INT PRIMARY KEY, 
username varchar(30) unique, 
author_name varchar(30))''')
conn.commit()

# insert into table
insert_db = "INSERT INTO author (id, username, author_name) VALUES (?, ?, ?)"

conn.execute(insert_db, (1, 'almasud', 'Abdullah Al Masud'))
conn.execute(insert_db, (2, 'rimon', 'Rimon Ali'))
conn.execute(insert_db, (3, 'niloy', 'Niloy Roy'))
conn.execute(insert_db, (4, 'sourav', 'Sourav Deb Sharma'))
conn.execute(insert_db, (5, 'sathi', 'Sathi Rani Roy'))

#
cur = conn.cursor()
cur.execute("SELECT id, author_name from author")
# conn.execute("SELECT id, author_name from author")
rows = cur.fetchall()

print(rows)
for row in rows:
    print(row[0], row[1], sep="-")