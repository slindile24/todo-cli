#DB connection and table creation
import sqlite3


#Here I am creating a table,this function is only used once at startup
def create_table():

    connection = sqlite3.connect('tasks.db')
    cursor = connection.cursor()

    cursor.execute("""CREATE TABLE IF NOT EXISTS tasks (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        title TEXT NOT NULL,
        description TEXT,
        completed INTEGER NOT NULL DEFAULT 0,
        created_at TEXT DEFAULT (datetime('now')),
        due_date TEXT,
        priority TEXT
    );
    """)
    connection.commit()
    connection.close()
    

create_table()

#This one is used later by other functions to open the same database and work with it.
def get_connection():
    conn =sqlite3.connect('data/tasks.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
get_connection()


def add_task(title,description=None,due_date=None,priority=None):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute(
        """ INSERT INTO tasks (title, description, due_date, priority)
            VALUES (?, ?, ?, ?)""",
            (title, description, due_date, priority)
    )
    
    conn.commit()
    conn.close()
add_task("Wash the dishes","Use hot water","2023-10-10","High")
   

