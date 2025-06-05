# To-Do List Application

todo_list = []

def add_task():
    task = input("Enter a task: ")
    todo_list.append({"task": task, "status": "pending"})
    print("New task added successfully.")

def view_tasks():
    print("\nYour To-Do List:")
    if not todo_list:
        print("No tasks in your to-do list.")
    else:
        for i, task in enumerate(todo_list, 1):
            print(f"{i}. {task['task']} - {task['status']}")

def mark_task_done():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to mark as done: "))
        if 1 <= task_num <= len(todo_list):
            todo_list[task_num - 1]["status"] = "done"
            print("Task marked as done.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def delete_task():
    view_tasks()
    try:
        task_num = int(input("Enter the task number to delete: "))
        if 1 <= task_num <= len(todo_list):
            removed_task = todo_list.pop(task_num - 1)
            print(f"Task '{removed_task['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Please enter a valid number.")

def menu():
    while True:
        print("\nMenu:")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")
        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_task()
        elif choice == '2':
            view_tasks()
        elif choice == '3':
            mark_task_done()
        elif choice == '4':
            delete_task()
        elif choice == '5':
            print("Exiting the to-do list application.")
            break
        else:
            print("Invalid choice. Please enter a number between 1 and 5.")

# Start the application
menu()
