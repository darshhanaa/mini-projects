tasks = []

def add_task():
    task = input("Enter task: ")
    tasks.append(task)
    print("Task added successfully!")

def view_tasks():
    if not tasks:
        print("No tasks found.")
        return

    print("\nTasks:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")

def remove_task():
    view_tasks()

    if tasks:
        index = int(input("Enter task number to remove: "))

        if 1 <= index <= len(tasks):
            removed = tasks.pop(index - 1)
            print(f"Removed: {removed}")
        else:
            print("Invalid task number.")

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        add_task()

    elif choice == "2":
        view_tasks()

    elif choice == "3":
        remove_task()

    elif choice == "4":
        break

    else:
        print("Invalid choice!")
