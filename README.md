# ✅ Task Manager CLI App

A command-line Task Management application built in Python with MySQL integration. It allows users to manage daily tasks with features like sorting, updating, and persistent storage. This project demonstrates the use of Python fundamentals, object-oriented programming (OOP), and raw SQL queries.

---

## 🚀 Features

- Add tasks with title, description, due date, priority, and status
- List tasks, sorted by due date or priority
- Update task details
- Mark tasks as completed
- Delete tasks
- Automatic timestamp on creation
- MySQL-backed persistent storage
- Built using Object-Oriented Programming principles
- No ORM — uses raw SQL queries
- Input validation and error handling

---

## 🛠️ Technologies Used

- Python 3.x
- MySQL
- `mysql-connector-python`
- Standard libraries: `datetime`, `os`, etc.

---

## 🧪 Setup Instructions

### 1. 📦 Install dependencies

```bash
pip install -r requirements.txt

2. 🛠️ Configure MySQL
Ensure you have MySQL running locally. Then update your db.py file with your credentials:

config = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "task_manager"
}

Then run the following command to create the database and table:
