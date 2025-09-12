# Browser-Based To-Do App (Flask + SQLAlchemy)

A **full-stack web application** that allows users to manage their personal tasks directly in the browser. Built using **Python, Flask, and SQLAlchemy**, this project demonstrates session-based user authentication, CRUD operations, and dynamic template rendering.

---

## **Tech Stack**
- **Backend:** Flask (Python)  
- **Database:** SQLAlchemy (SQLite)  
- **Frontend:** HTML, Jinja2 templates, Bootstrap / CSS  
- **Authentication:** Flask session for user login management  

---

## **Key Features**
- **User Registration & Login:** Secure session-based authentication.  
- **Task Management:** Add, view, update (toggle status), delete, and clear tasks.  
- **User-Specific Data:** Tasks are linked to the logged-in user.  
- **Interactive Interface:** Fully functional in the browser with real-time feedback.  
- **Notifications:** Flash messages for user actions like task added or deleted.  

---

## **Getting Started (PowerShell)**

### **Prerequisites**
- Python 3.x installed
- pip (Python package manager)

### **Installation & Run**
1. Clone the repository:
```powershell
git clone https://github.com/yourusername/TODO_APP.git
cd TODO_APP
```

2. Install dependencies:
```powershell
pip install -r requirements.txt
```

3. Run the application:

```powershell
$env:FLASK_APP = "TODO_APP"
$env:FLASK_ENV = "development"
flask run
```
4. Open your browser at http://127.0.0.1:5000

## Usage

1. Register a new account or log in with existing credentials.  
2. Add tasks using the task input form.  
3. Toggle task status: **Pending → Working → Done → Pending**.  
4. Delete individual tasks or clear all tasks at once.  
5. Tasks are saved and linked to your account.  

---

## Learning Outcomes

- Handling web forms and user input in Flask.  
- Implementing session-based authentication and authorization.  
- Dynamic template rendering with Jinja2.  
- CRUD operations with SQLAlchemy.  
- Managing user-specific data in a multi-user environment.  

---

## Author

- **Pawan Kumar**  
- GitHub: [https://github.com/pawan252003](https://github.com/pawan252003)



