
# ITC-345 Python Final Project - Group 6

A Flask-based Library Management System developed as a group project.  
This project combines the main library system with authentication features, so users can register, log in, manage books, and access the dashboard from one main Flask app.

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
- Authentication integrated into the main library system

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

---

## Why use a virtual environment (venv)?

A virtual environment keeps the packages for this project separated from the packages installed globally on your computer.

This is useful because:

* it prevents dependency conflicts
* it keeps the project clean
* it makes setup easier for all group members
* it avoids breaking other Python projects on your machine

---

## Requirements

Before running the project, make sure you have:

* Python 3 installed
* pip installed

You can check with:

```bash
python3 --version
pip --version
```

or on some systems:

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

After activation, you should see `(venv)` in your terminal.

---

## 4. Install dependencies with pip

Since the project file is named `requirements copy.txt`, install the dependencies with:

```bash
pip install -r "requirements copy.txt"
```

---

## 5. Install dependencies with uv (optional)

If you want, you can also use `uv`.

First install it:

```bash
pip install uv
```

Then install the project dependencies:

```bash
uv pip install -r "requirements copy.txt"
```

If you rename the file later to `requirements.txt`, then you can use:

```bash
uv pip install -r requirements.txt
```

---

## 6. Run the project

Run the main application with:

```bash
python run.py
```

or on some systems:

```bash
python3 run.py
```

Then open in your browser:

```bash
http://127.0.0.1:5000/
```

---

## Important

For the final integrated project, use:

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

Stored in:

```bash
instance/library.db
```

Used for:

* books
* main library data

### Auth database

Stored in:

```bash
auth/instance/library.db
```

Used for:

* users
* login and register authentication data

Both databases should remain in place.

If needed, create the folders manually:

```bash
mkdir -p instance
mkdir -p auth/instance
```

---

## Main Files to Know

### `run.py`

The main file used to start the full application.

### `config.py`

Contains the app configuration and database paths.

### `app/__init__.py`

Creates and configures the Flask app.

### `app/auth.py`

Handles login, register, and logout routes connected to the main app.

### `app/books.py`

Handles book-related pages and actions.

### `test_view.py`

Used only for testing templates. It is not the final integrated project file.

---

## Notes About the Project

* The `app/` folder contains the main integrated Flask application.
* The `auth/` folder still contains an older separate authentication version.
* The final project should be run from `run.py`.
* The authentication part is already connected to the main app through `app/auth.py`.
* The project currently uses SQLite for simplicity and easy local testing.

---

## Troubleshooting

### Virtual environment does not activate

On Windows PowerShell, if activation is blocked, try:

```bash
Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass
```

Then run:

```bash
venv\Scripts\Activate.ps1
```

### Flask or other packages are missing

Make sure the virtual environment is activated first, then run:

```bash
pip install -r "requirements copy.txt"
```

### Database folder does not exist

Create it manually:

```bash
mkdir -p instance
mkdir -p auth/instance
```

### Wrong file used to run the project

Use:

```bash
python run.py
```

Do not use `test_view.py` for the final project.

---

## Group Project

This project was developed as a group final project for ITC-345.
Different parts of the project were worked on by different group members, then combined into one final integrated Flask application.

---

## Final Reminder

To run the final integrated version of the project:

```bash
python run.py
```

and open:

```bash
http://127.0.0.1:5000/
```

