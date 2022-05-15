import sqlite3


db = sqlite3.connect('users.db')
db.isolation_level=None
db=db.cursor()



def get_database_connection():
    return db