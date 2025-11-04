import sqlite3
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