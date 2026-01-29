# file = "/Users/mac/Desktop/todo-list-cli/tasks.txt"
file = "tasks.txt"

def load_tasks():
    try:
        with open(file, "r") as f:
            tasks = []
            for line in f:
                task, status = line.strip().split(" | ")
                tasks.append({"task": task, "status": status})
            return tasks
    except FileNotFoundError:
        return []
    
def save_task(tasks):
    with open(file, "w")as f:
        for task in tasks:
            f.write(f"{task['task']} | {task['status']}\n")

def view_task(tasks):
    if not tasks:
        print("\nNo Tasks found.")
        return
    print("\nTo-Do List:")
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task['task']} - {task['status']}")
    print()

def add_task(tasks):
    new_task = input("\nEnter task: ")
    tasks.append({"task": new_task, "status": "Pending"})
    save_task(tasks)
    print("Task added succesfully.\n")

def mark_complete(tasks):
    view_task(tasks)
    try:
        choice = int(input("Enter task number to make complete: "))
        tasks[choice -1]["status"] = "Completed"
        save_task(tasks)
        print("Task marked as completed!\n")
    except:
        print("Envalid choice!\n")

def delete_task(tasks):
    view_task(tasks)
    try:
        choice = int(input("Enter task number to delete: "))
        tasks.pop(choice-1)
        save_task(tasks)
        print("Task deleted!\n")
    except:
        print("Envalid choice!\n")

def main():
    tasks = load_tasks()
    while True:
        print("1.View Tasks")
        print("2.Add Task")
        print("3.Mark Task as complete")
        print("4.Delete Task")
        print("5.Exit")

        choice = int(input("\nChoose an option:"))

        if choice == 1:
            view_task(tasks)
        elif choice == 2:
            add_task(tasks)
        elif choice == 3:
            mark_complete(tasks)
        elif choice == 4:
            delete_task(tasks)
        elif choice == 5:
            print("\nGoodbye!\n")
            break
        else :
            print("Invalid option!\n")

if __name__ == "__main__":
    main()
