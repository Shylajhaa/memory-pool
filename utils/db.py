from cmath import e
import mysql.connector

class DbUtil:
    def __init__(self) -> None:
        self.mydb = mysql.connector.connect(
            host="localhost",
            user="root",
            password="root",
            database="memory_pool"
        )
    
    def insert(self, query):
        cursor = self.mydb.cursor()
        cursor.execute(query)
        
        self.mydb.commit()
        print(cursor.rowcount, "Record inserted successfully")
        cursor.close()
    
    def select(self, query):
        cursor = self.mydb.cursor()
        cursor.execute(query)
        record = cursor.fetchall()

        return record

    def test(self):
        print(self.mydb)
