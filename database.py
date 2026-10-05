import sqlite3
DATABASE_NAME="tickets.db"
def get_db_connection():
    conn=sqlite3.connect(DATABASE_NAME)
    conn.row_factory=sqlite3.Row
    return conn
def init_db():
    conn=get_db_connection()
    cursor=conn.cursor()
    cursor.execute(""" 
                    CREATE TABLE IF NOT EXISTS tickets(id NUMBER PRIMARY KEY AUTOINCREMENT,title VARCHAR NOT NULL,description VARCHAR,
                    status VARCHAR DEFALUT "open",priority VARCHAR,created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP);""")
    conn.commit()
    conn.close()
    print("table created")
if __name__=="__main__":
    init_db()