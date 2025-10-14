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
from datetime import datetime


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
        input_res = input("Choose an option between 1-5: ")
        if input_res == "1":
            while True:
                title = input("Enter the task title: ").strip()
                if len(title) > 15:
                    print("Title cannot exceed 15 characters")
                    title = input("Enter the task title: ").strip()

                if not title:
                    print("Task title cannot be empty!")
                    title = input("Enter the task title: ").strip()
                break
          

            description = input("Enter the task description: ").strip()

            due_date = input("Enter the task due_date(YYYY-MM-DD): ").strip()
            while True:
                try:
                    due_date_str = datetime.strptime(due_date,"%Y-%m-%d")
                    return due_date_str
                except ValueError:
                    print("Invalid date format! Enter the correct format(YYYY-MM-DD)!")
                    due_date = input("Enter the task due_date(YYYY-MM-DD): ").strip()
                break


              
            priority = input("Enter the task priority(Low,Medium,High): ").strip()


            # if due_date != "YYYY-MM-DD":
            #     print("Enter a correct date format")


            # if not due_date:
            #     due_date = None

            if not priority:
                priority = "Low"

            add_task(title,description,due_date,priority)
            print(f"Task '{title}' added successfully! ")

        elif input_res == "2":
            print(display_tasks())

        elif input_res == "3":
            try:
                update_id = int(input("Enter the task ID you want to update: "))
                update_task(update_id)
                print(f"Task {update_id} is updated successfully and marked completed!")
            except ValueError:
                print("Enter a valid numeric value! ")

        elif input_res == "4":
            print(display_tasks())
            try:
                delete_id = int(input("Enter the task ID you want to delete: "))
                delete_task(delete_id)
                print(f"Task {delete_id} deleted successfully!")
            except ValueError:
                print("Enter a valid numeric value! ")

        elif input_res == "5":
            print("Exiting!")
            break
        else:
            print("Invalid choice. Pick the correct choice from the menu")

display_menu()
        
    
