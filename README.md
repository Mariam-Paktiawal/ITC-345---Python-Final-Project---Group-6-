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


<br><hr><br>

# 1. Clone the project

``` bash

git clone https://github.com/Mariam-Paktiawal/ITC-345---Python-Final-Project---Group-6-.git
cd ITC-345---Python-Final-Project---Group-6-

```

<br><hr><br>


# 2. Create the virtual environment

On Linux / macOS

```bash
python3 -m venv venv
```

On Windows

```bash
python -m venv venv
```

<br><hr><br>



# 3. Activate the virtual environment

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

After activation, you should see (venv) in the terminal.

<br><hr><br>




# 4. Install dependencies with pip

Since we have Requirements copy.txt have to :

```bash
requirements copy.txt
```
install with:

```bash
pip install -r "requirements copy.txt"
```

<br><hr><br>
## Python Environment and Running the Project

### 5. Install dependencies with uv (optional)

```bash
pip install uv
```

```bash
uv pip install -r "requirements copy.txt"
```

```bash
uv pip install -r requirements.txt
```

### 6. Run the project

Run the main application with:

```bash
python run.py
```

or on some systems:

```bash
python3 run.py
```

Then open in your browser:

```
http://127.0.0.1:5000/
```

### Important

For the final integrated project, use:

```bash
python run.py
```

Do not use:

```bash
python test_view.py
```

because test_view.py is only for testing templates and does not include the full integrated routes and blueprints.

### Database Notes

This project uses SQLite databases.

#### Main database

Stored in:

```
instance/library.db
```

Used for:

- books
- main library data

#### Auth database

Stored in:

```
auth/instance/library.db
```

Used for:

- users
- login/register authentication data

Both databases should remain in place.

If needed, create the folders manually:

If needed, create the folders manually:

```bash
mkdir -p instance
mkdir -p auth/instance
```

### Main Files to Know
