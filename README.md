# ITC-345 Python Final Project - Group 6

A Flask-based Library Management System developed as a group project.  
This project combines a main library system with authentication features, allowing users to register, log in, manage books, and access the dashboard from one main Flask app.

---

## Project Overview

This application includes:

- User registration
- User login and logout
- Dashboard
- Book listing
- Book details
- Add book
- Edit book
- Delete book
- Search and filtering for books
- SQLite database support
- Authentication integration with the main library system

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
├── test_view.py                 # Template test file (not for final app)
├── requirements copy.txt        # Project dependencies
├── README.md
└── tests/
```


# Why use a virtual environment (venv)?

A virtual environment keeps the packages for this project separated from the packages installed globally on your computer.

This helps because:

* it prevents dependency conflicts
* it keeps the project clean
* it makes setup easier for all group members
* it avoids breaking other Python projects on your machine


<hr><br>

# Requirements

Before running the project, make sure you have:
* Python 3 installed
* pip installed


Check with:

```bash
python3 --version
pip --version
```
or:

```bash
python --version
pip3 --version
```




# 1. Clone the project

``` bash

git clone https://github.com/Mariam-Paktiawal/ITC-345---Python-Final-Project---Group-6-.git
cd ITC-345---Python-Final-Project---Group-6-

```