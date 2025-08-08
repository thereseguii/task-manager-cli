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

    def add_task(self, title, description, due_date, priority):
        task = Task(self.task_counter, title, description, due_date, priority)
        self.db.insert_task(task)
        print(f"✅ Task [{self.task_counter}] added successfully.")
        self.task_counter += 1

    def list_tasks(self):
        tasks = self.db.fetch_all()
        print("\n📋 Task List:")
        for t in tasks:
            print(f"[{t[0]}] {t[1]} | {t[5]} | Due: {t[3]} | Priority: {t[4]}")

    def close(self):
        self.db.close()
