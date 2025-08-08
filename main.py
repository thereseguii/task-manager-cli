from task_manager import TaskManager

def main():
    manager = TaskManager()

    while True:
        print("\n==== Task Manager ====")
        print("1. Add Task")
        print("2. List Tasks")
        print("3. Exit")
        choice = input("Select an option (1-3): ")

        if choice == "1":
            title = input("Title: ")
            desc = input("Description: ")
            due = input("Due Date (YYYY-MM-DD): ")
            priority = input("Priority (Low, Medium, High): ")
            manager.add_task(title, desc, due, priority)
        elif choice == "2":
            manager.list_tasks()
        elif choice == "3":
            manager.close()
            print("👋 Exiting Task Manager.")
            break
        else:
            print("❌ Invalid option. Please try again.")

if __name__ == "__main__":
    main()
