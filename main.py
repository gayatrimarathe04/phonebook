import sqlite3

db = sqlite3.connect('contacts.db')

cur = db.cursor()

db.commit()
db.close()


