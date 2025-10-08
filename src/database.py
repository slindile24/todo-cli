#DB connection and table creation
import sqlite3


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
add_task("Stand-up meeting","Meeting with team","2023-10-11","High")

def get_all_tasks():
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""SELECT * FROM tasks""") # This doesn't retrieve data but it just prepares the sql query
    tasks = cursor.fetchall()   # the fetchall() is used to retrieve data from the database,returns all rows
    conn.close()    # the fetchall() returns a list of tuples , where each tuple represents one row
    return tasks


def display_tasks():
    tasks = get_all_tasks()
    if not tasks:
        print("No tasks found.")
        return
    
    for task in tasks:
        task_id, title, description, completed, created_at, due_date, priority= task
        print(f"""

            ID: {task_id}
            Title: {title}
            Description: {description or "None"}
            Due Date : {due_date or "None"}
            Priority: {priority or "None"}
            Completed: {"Yes" if completed  else "No"}
            Created At: {created_at}

""")
 
display_tasks()


   

