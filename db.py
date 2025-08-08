import mysql.connector
from mysql.connector import Error

class Database:
    def __init__(self):
        try:
            self.conn = mysql.connector.connect(
                host="localhost",
                user="root",               
                password="MiggyMiggy21!",               
                database="task_manager_db" 
            )
            self.cursor = self.conn.cursor()
        except Error as e:
            print(f"❌ Error connecting to MySQL: {e}")
            exit(1)

    def create_table(self):
        create_query = """
        CREATE TABLE IF NOT EXISTS tasks (
            task_id INT PRIMARY KEY,
            title VARCHAR(255),
            description TEXT,
            due_date DATE,
            priority VARCHAR(20),
            status VARCHAR(20),
            created_at DATETIME
        );
        """
        self.cursor.execute(create_query)
        self.conn.commit()

    def insert_task(self, task):
        insert_query = """
        INSERT INTO tasks (task_id, title, description, due_date, priority, status, created_at)
        VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        self.cursor.execute(insert_query, (
            task.task_id,
            task.title,
            task.description,
            task.due_date,
            task.priority,
            task.status,
            task.created_at
        ))
        self.conn.commit()

    def fetch_all(self):
        self.cursor.execute("SELECT * FROM tasks")
        return self.cursor.fetchall()

    def close(self):
        self.conn.close()
