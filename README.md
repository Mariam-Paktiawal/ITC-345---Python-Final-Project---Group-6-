# ITC-345 Python Final Project - Group 6

This is our final group project for ITC-345.  
It is a Flask-based Library Management System. In this project, we combined the main library system with the authentication system, so the user can register, log in, log out, manage books, and access the dashboard from one main app.


# Contributors

- Mariam Paktiawal: Database and Models, Github Repository
- Diba Nasimi: Authentication and User Management
- Ghulam Mahfoz Osmani: Book Management and Search, Documentation
- Mahrukh Mohammadi: Design of Website, Testing 
---

## Project Overview

This project includes:

- User registration
- User login
- User logout
- Dashboard
- Book listing
- Book details
- Add book
- Edit book
- Delete book
- Search and filtering for books
- SQLite database support
- Authentication connected to the main library system

---

## Project Structure

```bash
ITC-345---Python-Final-Project---Group-6-/
│
├── app/                         # Main Flask application
│   ├── __init__.py              # App factory
│   ├── auth.py                  # Auth routes connected to main app
│   ├── books.py                 # Book routes
│   ├── loans.py
│   ├── users.py
│   ├── models.py                # Main database models
│   └── templates/               # Main templates
│
├── auth/                        # Older separate auth files + auth database
│   ├── app.py
│   ├── auth.py
│   ├── models.py
│   ├── instance/
│   │   └── library.db
│   ├── templates/
│   └── requirements.txt
│
├── instance/                    # Main SQLite database folder
│   └── library.db
│
├── config.py                    # Configuration file
├── run.py                       # Main file to run the project
├── test_view.py                 # Template test file
├── requirements copy.txt        # Project dependencies
├── README.md
└── tests/
```

---

## Why use a virtual environment?

We use a virtual environment because it keeps the packages for this project separated from the global Python packages installed on the computer.

This helps because:

* it avoids conflicts between packages
* it keeps the project cleaner
* it makes the setup easier for all group members
* it does not affect other Python projects on the same computer

---

## Requirements

Before running the project, make sure you already have:

* Python 3 installed
* pip installed

You can check with:

```bash
python3 --version
pip --version
```

or:

```bash
python --version
pip3 --version
```

---

## 1. Clone the project

```bash
git clone https://github.com/Mariam-Paktiawal/ITC-345---Python-Final-Project---Group-6-.git
cd ITC-345---Python-Final-Project---Group-6-
```

> Note: if the repository is private, only users with access can clone it.

---

## 2. Create the virtual environment

### On Linux / macOS

```bash
python3 -m venv venv
```

### On Windows

```bash
python -m venv venv
```

---

## 3. Activate the virtual environment

### On Linux / macOS

```bash
source venv/bin/activate
```

### On Windows CMD

```bash
venv\Scripts\activate
```

### On Windows PowerShell

```bash
venv\Scripts\Activate.ps1
```

After activation, you should see `(venv)` in the terminal.

---

## 4. Install dependencies

Because our file is named `requirements copy.txt`, install the dependencies with:

```bash
pip install -r "requirements copy.txt"
```

---

## 5. Optional: install dependencies with uv

If you want, you can also use `uv`.

First install it:

```bash
pip install uv
```

Then install the dependencies with:

```bash
uv pip install -r "requirements copy.txt"
```

---

## 6. Run the project

To run the final integrated project, use:

```bash
python run.py
```

or on some systems:

```bash
python3 run.py
```

Then open this in your browser:

```text
http://127.0.0.1:5000/
```

---

## Important Note

For the final integrated version of the project, use:

```bash
python run.py
```

Do **not** use:

```bash
python test_view.py
```

because `test_view.py` is only for testing templates and does not include the full integrated routes and blueprints.

---

## Database Notes

This project uses SQLite databases.

### Main database

Path:

```text
instance/library.db
```

This database is used for:

* books
* main library data

### Auth database

Path:

```text
auth/instance/library.db
```

This database is used for:

* users
* login and registration authentication data

Both databases should stay in place.

If the folders do not exist, you can create them manually.

### On Linux / macOS

```bash
mkdir -p instance
mkdir -p auth/instance
```

### On Windows

```bash
mkdir instance
mkdir auth\instance
```

---

## Main Files

### `run.py`

This is the main file used to run the whole project.

### `config.py`

This file contains the app configuration and database paths.

### `app/__init__.py`

This file creates and configures the Flask application.

### `app/auth.py`

This file contains the authentication routes connected to the main app.

### `app/books.py`

This file handles the book pages and book actions.

### `test_view.py`

This file is only for testing templates, not for running the final integrated project.

---

## About the Project

* The `app/` folder contains the main integrated Flask application.
* The `auth/` folder still contains the older separate authentication files.
* The final project should be started from `run.py`.
* Authentication is connected to the main app through `app/auth.py`.
* SQLite is used because it is simple and easy for local project testing.

---

## Troubleshooting

### Virtual environment does not activate on PowerShell

Try this first:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then activate again:

```bash
venv\Scripts\Activate.ps1
```

### Missing packages

Make sure the virtual environment is activated, then run:

```bash
pip install -r "requirements copy.txt"
```

### Missing database folders

Create them manually.

#### On Linux / macOS

```bash
mkdir -p instance
mkdir -p auth/instance
```

#### On Windows

```bash
mkdir instance
mkdir auth\instance
```

### Project not working when using `test_view.py`

That is normal for the final project, because `test_view.py` is not the complete integrated application.

Use:

```bash
python run.py
```

---

## Group Project Note

This project was developed as a group final project. Different members worked on different parts, and in the end the parts were combined into one final Flask application.

---

## Final Reminder

To run the final version of the project:

```bash
python run.py
```

Then open:

```text
http://127.0.0.1:5000/
```
