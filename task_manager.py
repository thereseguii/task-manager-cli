from task import Task
from db import Database

class TaskManager:
    def __init__(self):
        self.db = Database()
        self.db.create_table()
        self.task_counter = self.get_next_id()

    def get_next_id(self):
        tasks = self.db.fetch_all()
        if tasks:
            return max(t[0] for t in tasks) + 1
        return 1

    def add_task(self):
        title = input("Title: ")
        description = input("Description: ")
        due_date = input("Due Date (YYYY-MM-DD): ")
        priority = input("Priority (Low, Medium, High): ").capitalize()

        task = Task(self.task_counter, title, description, due_date, priority)
        self.db.insert_task(task)  # Make sure `insert_task()` exists in db.py
        print(f"\n✅ Task [{task.task_id}] added successfully.")
        self.task_counter += 1

        input("\nPress Enter to return to the menu...")

    def list_tasks(self):
        print("\n📋 Task List:")
        print("Sort by:")
        print("1. Due Date")
        print("2. Priority")
        print("3. Status")
        print("4. No Sorting")
        sort_option = input("Choose sort option (1-4): ").strip()

        query = "SELECT * FROM tasks"
        order_by = ""

        if sort_option == "1":
            order_by = " ORDER BY due_date ASC"
        elif sort_option == "2":
            order_by = """ ORDER BY 
                CASE priority
                    WHEN 'High' THEN 1
                    WHEN 'Medium' THEN 2
                    WHEN 'Low' THEN 3
                END ASC
            """
        elif sort_option == "3":
            status_filter = input("Enter status to filter (Pending, In Progress, Completed): ").title()
            query += f" WHERE status = '{status_filter}'"

        query += order_by

        try:
            self.db.cursor.execute(query)
            tasks = self.db.cursor.fetchall()

            if not tasks:
                print("No tasks found.")
                return

            for task in tasks:
                print(f"[{task[0]}] {task[1]} | {task[6]} | Due: {task[3]} | Priority: {task[4]}")
        except Exception as e:
            print(f"❌ Error: {e}")

    def close(self):
        self.db.close()
