import sqlite3
from sentence_transformers import SentenceTransformer

model = SentenceTransformer("all-MiniLM-L6-v2")

DBfile = 'Codeoftheday.db'
Used_db = 'used_database.db'

COD = sqlite3.connect(DBfile)
print("Database Sqlite3.db formed.")

c = COD.cursor()

class SQL_input:
    def __init__(self,Code,Answer):
        c.execute(''' CREATE TABLE IF NOT EXISTS New_Code_Base (
                      id INTEGER PRIMARY KEY AUTOINCREMENT,
                      code_snippet TEXT NOT NULL,
                      answer_text TEXT NOT NULL,
                      answer_embedding BLOB) ''')

        self.code = Code
        self.answer = Answer
        embedding_vector = model.encode([Answer])[0]  # [0] to get the first (and only) vector
        embedding_bytes = embedding_vector.tobytes()

        c.execute(''' INSERT INTO New_Code_Base (code_snippet, answer_text, answer_embedding) VALUES (?,?,?)''',(self.code, self.answer, embedding_bytes))
        ##now here we wirite the code for that wwhatever the answer we write turn it into a vector embedding.
COD.commit()
COD.close()