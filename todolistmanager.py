# Syntexhub Internship Project
# Project 3: To-Do List Manager
# Developed by Bisma Majid

import json

FILE_NAME = "tasks.json"

def load_tasks():
    try:
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    except:
        return []

def save_tasks(tasks):
    with open(FILE_NAME, "w") as file:
        json.dump(tasks, file)

def view_tasks(tasks):
    if not tasks:
        print("No tasks available.")
    else:
        for i, task in enumerate(tasks):
            status = "Done" if task["done"] else "Pending"
            print(f"{i+1}. {task['task']} - {status}")

def add_task(tasks):
    task_name = input("Enter new task: ")
    tasks.append({"task": task_name, "done": False})
    save_tasks(tasks)
    print("Task added successfully!")

def mark_done(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to mark done: "))
        tasks[num-1]["done"] = True
        save_tasks(tasks)
        print("Task marked as done!")
    except:
        print("Invalid selection.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num-1)
        save_tasks(tasks)
        print("Task deleted!")
    except:
        print("Invalid selection.")


def main():
    tasks = load_tasks()

    while True:
        print("\n===== TO-DO LIST MANAGER =====")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Enter choice (1-5): ")

        if choice == '1':
            view_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            print("Exiting To-Do Manager.")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()
