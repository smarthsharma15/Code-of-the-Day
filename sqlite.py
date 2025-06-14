import sqlite3

DBfile = 'Codeoftheday.db'
Used_db = 'used_database.db'

COD = sqlite3.connect(DBfile)
print("Database Sqlite3.db formed.")

c = COD.cursor()

class SQL_input:
    def __init__(self,Code,Answer):
        c.execute(''' CREATE TABLE IF NOT EXISTS Code_Base (
          Code TEXT NOT NULL,
          Answer TEXT NOT NULL 
          ) ''')
        self.code = Code
        self.answer = Answer
        c.execute(''' INSERT INTO Code_Base (Code,Answer) VALUES (?,?)''',(self.code,self.answer))


COD.commit()
COD.close()