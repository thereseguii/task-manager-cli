# ✅ Task Manager CLI App
A command-line interface (CLI) application for managing daily tasks. Built with Python and MySQL, this project demonstrates fundamental programming concepts, Object-Oriented Programming (OOP), and the use of raw SQL queries for persistent storage without an ORM.

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

## 📦 Setup Instructions

### 1. 🧪 Install dependencies

```
pip install -r requirements.txt
```
### 2. 🛠️ Configure MySQL

Ensure that MySQL is running locally on your machine. Then update your database credentials in the db.py file.

Open db.py and replace the placeholders with your actual MySQL username and password:

```
config = {
    "host": "localhost",
    "user": "your_username",       # Replace this
    "password": "your_password",   # Replace this
    "database": "task_manager"
}
```
Then run the following command to create the database and table:
```
python db.py
```

### 3. 🚀 Run the App

To launch the task manager, run:
```
python main.py
```

Use the menu to interact with the app from the command line.

### Notes

- Do not commit the venv or __pycache__ directories (they are excluded via .gitignore)
- Database errors are handled with user-friendly messages
- Code follows PEP 8 guidelines and includes comments/docstrings

### 🙋‍♀️ Author
Therese Segui
🔗 github.com/thereseguii
📧 therese.serranosegui@gmail.com

