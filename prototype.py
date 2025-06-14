## ctime = Thu Jan  1 05:30:00 1970
import time
import random
import sqlite3

## So till now we can put one whatever we print on screen into the 2n table called the used_base and its created in the same database not in the second databse
## things that remain or it to be complete ,First lets find a way to input answers and match it wiht the answer of th question printed on screen, It is still just doning this for the code column and not the answer one so gotta inplement that, 
### no way to write of check answers,
DBfile = 'Codeoftheday.db'
Used_db = 'useddatabase.db' 
COD = sqlite3.connect(DBfile)
print("Database Sqlite3.db formed.")

c = COD.cursor()

# Get data from Code_Base
c.execute('''SELECT A.Code FROM Code_Base as A 
            LEFT JOIN Used_base as B
          ON A.Code = B.Code
          Where B.code is null          
          Order by Random()''')
data = c.fetchone()
print(data)

answer = input("Please Enter Your Answer: ")
c.execute('''IF EXISTS(Select Answer )''')
c.execute(f"Select Answer From Code_Base Where Answer ='{answer}'")

# Insert the actual data (not NULL) into Used_base
c.execute('INSERT INTO Used_base (Code) VALUES (?);', (data[0],))
print("Code in used_base")



COD.commit()
COD.close()

#####Where i see this going (dont delete)

## now we want to read the database
## i am condidering a few things
###1. Make istead of used.txt turn it into another Database
### 2. We dont need the currect code now cause hat was teh logic for reading from a tuple of senteces  no we need to read cia db to put it back in the database (I.e Read from Codeoftheday.db and thn the things that are read once put it in a used.db)
#### here i am thinking of also taking other approach maybe that if the answer is wrong then it does not go into used.db something like that but currently lets startwith putting everything from codeof...db to used.db
