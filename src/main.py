#CLI entrypoint
# this file is made for building the command line interface
"""so instead of running functions manually the user can type
commands like
1. Add task
2. View tasks
3. Complete a task
4. Delete a task
5. Exit
 """
from database import *


def display_menu():

# (title, description, due_date, priority)
    while True:
        menu = """=== To-Do List ===
            1. Add a task
            2. View tasks
            3. Mark task as completed
            4. Delete task
            5. Exit
            """
        print(menu)
        input_res = input("Choose an option between 1-5:")
        if input_res == "1":
            add_task("Study","Study with friend","2023-10-13","High")
        elif input_res == "2":
            print(display_tasks())
        elif input_res == "3":
            print(update_task(6))
        elif input_res == "4":
            print(delete_task(1))
        elif input_res == "5":
            print("Exiting!")
            break
        else:
            print("Invalid choice. Pick the correct choice from the menu")
display_menu()
        
    
