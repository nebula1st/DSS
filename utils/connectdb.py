import mysql.connector

class ConnectDB():
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
    def Connect(self):    
        db = mysql.connector.connect(
            host='localhost',
            user='root',
            password='',
            database='spkkaryawanterbaik'
        )
        return db
