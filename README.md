# python-learning-journey
Learning Python from the ground up

# 🐍 Python Learning Journey

Welcome to my structured path for learning Python — from the basics to web development with CGI and Flask.  
This repository is both a **learning journal** and a **reference library**, showing my progression step by step.


![Security Badge](https://img.shields.io/badge/Secrets-managed%20via%20.env%20%2B%20.gitignore-brightgreen)

A structured learning project covering Python basics through databases and web integration.  
Sensitive credentials are **never committed** — they are managed securely using `.env` files and excluded from Git with `.gitignore`.

---

## 📂 Project Structure

```text
python-learning-journey/
├── 01_basics/
│   ├── hello_world.py
│   ├── variables.py
│   ├── input_output.py
│   └── math_operations.py
├── 02_control_flow/
│   ├── if_else.py
│   ├── loops.py
│   └── break_continue.py
├── 03_functions/
│   ├── functions_intro.py
│   ├── lambda_functions.py
│   ├── scope.py
│   ├── docstrings.py
│   ├── args_kwargs.py
│   └── recursion_examples.py
├── 04_oop/
│   ├── classes_objects.py
│   ├── inheritance.py
│   ├── polymorphism.py
│   ├── encapsulation.py
│   └── class_methods_static.py
├── 05_web_basics/
│   ├── cgi_hello.py
│   ├── cgi_form.py
│   ├── cgi_env.py
│   └── cgi_error.py
├── 06_flask_intro/
│   ├── app.py
│   ├── form_demo.py
│   └── templates/
│       ├── home.html
│       ├── about.html
│       └── contact.html
├── 07_databases/
│   ├── mysql_demo.py
│   └── templates/
│       └── users.html
└── README.md
```

## 01_basics
- `hello_world.py` → Prints "Hello World" to demonstrate Python’s simplest output.
- `variables_demo.py` → Shows variable assignment and basic data types.
- `loops_demo.py` → Demonstrates `for` and `while` loops with simple examples.

## 02_data_structures
- `list_examples.py` → Basic list operations: append, slice, iterate.
- `dict_examples.py` → Key/value storage and retrieval with dictionaries.
- `set_examples.py` → Demonstrates uniqueness and set operations.

## 03_functions_and_modules
- `functions_demo.py` → Defines and calls functions with parameters and return values.
- `modules_demo.py` → Imports built‑in modules and shows modular code structure.

## 04_oop
- `class_demo.py` → Defines a simple class with attributes and methods.
- `inheritance_demo.py` → Demonstrates subclassing and method overriding.
- `polymorphism_demo.py` → Shows how different classes can share behavior.

## 05_web_basics
- `cgi_hello.py` → A simple “Hello World” CGI script that outputs static HTML.
- `cgi_form.py` → Handles user input from an HTML form and dynamically responds.
- `cgi_env.py` → Displays CGI environment variables passed by Apache.
- `cgi_error.py` → Demonstrates error handling in CGI scripts.

## 06_flask_intro
- `app.py` → Flask app with multiple routes (`/`, `/about`, `/contact`) demonstrating navigation and template rendering.
- `templates/home.html` → Home page template with links to About and Contact.
- `templates/about.html` → About page template describing the app.
- `templates/contact.html` → Contact form template that accepts name, email, and message, and displays a confirmation.
- `form_demo.py` → Standalone script demonstrating GET/POST form handling directly with `render_template_string`.

## 07_databases

This section introduces database integration with Flask using **MySQL**.

### Files
- `mysql_demo.py` → Flask app that connects to MySQL using `mysqlclient` (`MySQLdb`) and environment variables for credentials.
- `templates/users.html` → Template that lists users retrieved from the database.

### Setup
1. Create the database and table in MySQL:
   ```sql
   CREATE DATABASE python_learning;
   USE python_learning;

   CREATE TABLE users (
       id INT AUTO_INCREMENT PRIMARY KEY,
       name VARCHAR(80)
   );

   INSERT INTO users (name) VALUES ('Alice'), ('Bob'), ('Charlie');

   ## Database Configuration & Security

This project uses a `config.py` file to manage database connection settings.  
Sensitive information such as usernames and passwords are **never committed to Git**. Instead, they are stored in a local `.env` file and loaded at runtime using [python-dotenv](https://pypi.org/project/python-dotenv/).

### How it works
- `.env` contains environment variables (e.g., `MYSQL_USER`, `MYSQL_PASSWORD`).
- `config.py` loads these variables securely with `dotenv`.
- `.gitignore` excludes both `config.py` and `.env` to prevent accidental commits.

### Example `.env`
```env
MYSQL_HOST=localhost
MYSQL_USER=root
MYSQL_PASSWORD=your_secure_password
MYSQL_DATABASE=python_learning


---

## ✅ Why This Helps
- Shows recruiters you understand **security and reproducibility**.
- Makes it clear collaborators should set up their own `.env` file.
- Reinforces that your repo is clean — no secrets in history.

---

Perfect — here’s a concise **Setup Instructions** section you can drop into your README so collaborators (or recruiters) know exactly how to run your database demo securely:

---

## ⚙️ Setup Instructions

To run the database examples in `07_databases`, follow these steps:

1. **Install dependencies**
   ```bash
   pip install python-dotenv mysql-connector-python
   ```

2. **Create a `.env` file** at the project root (same level as `README.md`):
   ```env
   MYSQL_HOST=localhost
   MYSQL_USER=root
   MYSQL_PASSWORD=your_secure_password
   MYSQL_DATABASE=python_learning
   ```

3. **Verify `.gitignore`** excludes sensitive files:
   ```
   07_databases/config.py
   .env
   ```

4. **Run the demo**
   ```bash
   python 07_databases/mysql_demo.py
   ```

5. **Confirm environment variables are loaded**
   ```bash
   python -c "import config; print(config.MYSQL)"
   ```
   → should print your connection dictionary with values from `.env`.

---

## ✅ Why This Helps
- Keeps credentials out of GitHub history.  
- Makes setup reproducible for anyone cloning your repo.  
- Shows recruiters you understand secure, professional workflows.  

---
