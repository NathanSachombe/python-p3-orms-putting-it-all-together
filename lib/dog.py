import sqlite3

CONN = sqlite3.connect('lib/dogs.db')
CURSOR = CONN.cursor()

class Dog:
     
    def __init__(self, name, breed):
        self.id = None
        self.name = name
        self.breed = breed
    
    @classmethod
    def create_table(self):
        sql = """"
            CREATE TABLE IF NOT EXISTS dogs (
                id INTEGER PRIMARY KEY,
                name TEXT,
                breed TEXT
                )
                """
        CURSOR.execute(sql)

    @classmethod
    def drop_table(self):
        sql = """
              DROP TABLE IF EXISTS songs
              """
        CURSOR.execute(sql)  
    
    def save(self):
        sql = """
             INSERT INTO dogs (name, breed)
             VALUES (?, ?)
             """
        CURSOR.execute(sql, (self.name, self.breed))

    


    

