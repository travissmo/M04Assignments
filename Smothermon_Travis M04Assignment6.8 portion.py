import sqlalchemy 
import csv
import sqlite3

connection = sqlite3.connect('books.db')
cursor = connection.cursor()
#Use if not exists to prevent redundant data also defining the data types 
cursor.execute ('''  CREATE TABLE IF NOT EXISTS books ( 
        title TEXT,
        author TEXT,
        year INTEGER
    )
''')


#Data that will be inserted into the table
books_data = [
    ["title", "author", "year"],
    ["The Weirdstone of Brisingamen", "Alan Garner", 1960],
    ["Perdido Street Station", "China Miéville", 2000],
    ["Thud!", "Terry Pratchett", 2005],
    ["The Spellman Files", "Lisa Lutz", 2007],
    ["Small Gods", "Terry Pratchett", 1992],
]
#Found execute many when getting help with this part lets you insert the books data in one go
cursor.executemany('''
    INSERT INTO books (title, author, year) 
    VALUES (?, ?, ?)
''', books_data)

connection.commit()

cursor.execute("SELECT * FROM books")


results = cursor.fetchall()


for row in results:
    print(row)

