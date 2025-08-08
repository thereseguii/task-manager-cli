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

### 2. 🛠️ Configure MySQL
Ensure you have MySQL running locally. Then update your db.py file with your credentials:

config = {
    "host": "localhost",
    "user": "your_username",
    "password": "your_password",
    "database": "task_manager"
}
Then run the following command to create the database and table:

python db.py

## 3. 🚀 Run the App

python main.py

Use the menu to interact with the app from the command line.

### 🧹 Notes
Do not commit the venv or __pycache__ directories (excluded via .gitignore)

Database errors are handled with user-friendly messages

Code follows PEP 8 guidelines and includes comments/docstrings


## 🙋‍♀️ Author
Therese Segui
🔗 github.com/thereseguii
📧 therese.serranosegui@gmail.com
