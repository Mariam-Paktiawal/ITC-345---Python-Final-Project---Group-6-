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