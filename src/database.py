#DB connection and table creation
import sqlite3


#This one is used later by other functions to open the same database and work with it.
def get_connection():
    conn =sqlite3.connect('data/tasks.db')
    conn.execute("PRAGMA foreign_keys = ON;")
    return conn
get_connection()


# def add_task(title,description=None,due_date=None,priority=None):
#     conn = get_connection()
#     cursor = conn.cursor()
#     cursor.execute(
#         """ INSERT INTO tasks (title, description, due_date, priority)
#             VALUES (?, ?, ?, ?)""",
#             (title, description, due_date, priority)
#     )
#     conn.commit()
#     conn.close()
# add_task("Study","Study with friend","2023-10-13","High")

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
 
# display_tasks()


def update_task(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""UPDATE tasks SET completed = 1 WHERE  id= ?""",(id,))  
    conn.commit()    #this saves the change
    conn.close()

    #passed tuple with one element like this (id,) because if i pass it like this(id) then it's an integer   


def delete_task(id):
    conn = get_connection()
    cursor = conn.cursor()
    cursor.execute("""DELETE FROM tasks WHERE id = ?""",(id,))
    conn.commit()
    conn.close()



#adding a test call to test my functions if they work
if __name__ == "__main__":
    # update_task(2)
    delete_task(3)
    print("Deleted task 3 from the table")
