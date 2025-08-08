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
            manager.add_task()  # ✅ This function handles inputs itself now
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
