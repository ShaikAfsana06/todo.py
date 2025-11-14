import json
import os

TODO_FILE = "todos.json"


def load_tasks():
    if not os.path.exists(TODO_FILE):
        return []
    with open(TODO_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(TODO_FILE, "w") as f:
        json.dump(tasks, f, indent=4)


def show_menu():
    print("\n==== To-Do List Manager ====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Mark Task as Completed")
    print("4. Delete Task")
    print("5. Exit")


def add_task(tasks):
    task = input("Enter task: ").strip()
    if task:
        tasks.append({"task": task, "done": False})
        save_tasks(tasks)
        print("Task added.")
    else:
        print("Empty task not allowed.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return

    print("\nYour Tasks:")
    for i, t in enumerate(tasks, start=1):
        status = "✔" if t["done"] else "✗"
        print(f"{i}. [{status}] {t['task']}")


def mark_complete(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to mark complete: "))
        tasks[num - 1]["done"] = True
        save_tasks(tasks)
        print("Task marked as completed.")
    except:
        print("Invalid input.")


def delete_task(tasks):
    view_tasks(tasks)
    if not tasks:
        return
    try:
        num = int(input("Enter task number to delete: "))
        tasks.pop(num - 1)
        save_tasks(tasks)
        print("Task deleted.")
    except:
        print("Invalid input.")


def main():
    tasks = load_tasks()

    while True:
        show_menu()
        choice = input("Select an option: ")

        if choice == "1":
            add_task(tasks)
        elif choice == "2":
            view_tasks(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
