import os
import sqlite3

from flask import (
    Blueprint,
    current_app,
    flash,
    redirect,
    render_template,
    request,
    url_for
)
from flask_login import (
    UserMixin,
    current_user,
    login_required,
    login_user,
    logout_user
)
from werkzeug.security import check_password_hash, generate_password_hash

auth_bp = Blueprint("auth", __name__)


class SessionUser(UserMixin):
    def __init__(self, user_id, username, email, role="user"):
        self.id = str(user_id)
        self.username = username
        self.email = email
        self.role = role


def get_auth_db_path():
    return current_app.config["AUTH_DB_PATH"]


def ensure_auth_db_exists():
    db_path = get_auth_db_path()
    os.makedirs(os.path.dirname(db_path), exist_ok=True)

    conn = sqlite3.connect(db_path)
    conn.execute(
        """
        CREATE TABLE IF NOT EXISTS user (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            username VARCHAR(100) NOT NULL,
            email VARCHAR(120) NOT NULL UNIQUE,
            password_hash VARCHAR(255) NOT NULL,
            role VARCHAR(20) NOT NULL DEFAULT 'user'
        )
        """
    )
    conn.commit()
    conn.close()


def get_auth_connection():
    ensure_auth_db_exists()
    conn = sqlite3.connect(get_auth_db_path())
    conn.row_factory = sqlite3.Row
    return conn


def get_auth_user_by_id(user_id):
    conn = get_auth_connection()
    row = conn.execute(
        "SELECT id, username, email, role FROM user WHERE id = ?",
        (user_id,)
    ).fetchone()
    conn.close()
    return row


def get_auth_user_by_email(email):
    conn = get_auth_connection()
    row = conn.execute(
        "SELECT id, username, email, password_hash, role FROM user WHERE email = ?",
        (email,)
    ).fetchone()
    conn.close()
    return row


def create_auth_user(username, email, password):
    password_hash = generate_password_hash(password)

    conn = get_auth_connection()
    conn.execute(
        """
        INSERT INTO user (username, email, password_hash, role)
        VALUES (?, ?, ?, ?)
        """,
        (username, email, password_hash, "user")
    )
    conn.commit()
    conn.close()


def load_auth_user(user_id):
    row = get_auth_user_by_id(user_id)
    if not row:
        return None

    return SessionUser(
        user_id=row["id"],
        username=row["username"],
        email=row["email"],
        role=row["role"]
    )


@auth_bp.route("/register", methods=["GET", "POST"])
def register():
    if current_user.is_authenticated:
        return redirect(url_for("auth.dashboard"))

    if request.method == "POST":
        username = request.form.get("username", "").strip()
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()

        if not username or not email or not password:
            flash("All fields are required.", "warning")
            return redirect(url_for("auth.register"))

        existing_user = get_auth_user_by_email(email)
        if existing_user:
            flash("This email is already registered.", "danger")
            return redirect(url_for("auth.register"))

        create_auth_user(username, email, password)

        flash("Registration successful. Please log in.", "success")
        return redirect(url_for("auth.login"))

    return render_template("register.html")


@auth_bp.route("/login", methods=["GET", "POST"])
def login():
    if current_user.is_authenticated:
        return redirect(url_for("auth.dashboard"))

    if request.method == "POST":
        email = request.form.get("email", "").strip().lower()
        password = request.form.get("password", "").strip()

        if not email or not password:
            flash("Email and password are required.", "warning")
            return redirect(url_for("auth.login"))

        user_row = get_auth_user_by_email(email)

        if not user_row:
            flash("Invalid email or password.", "danger")
            return redirect(url_for("auth.login"))

        if not check_password_hash(user_row["password_hash"], password):
            flash("Invalid email or password.", "danger")
            return redirect(url_for("auth.login"))

        session_user = SessionUser(
            user_id=user_row["id"],
            username=user_row["username"],
            email=user_row["email"],
            role=user_row["role"]
        )

        login_user(session_user)
        flash("Login successful.", "success")
        return redirect(url_for("auth.dashboard"))

    return render_template("login.html")


@auth_bp.route("/logout")
@login_required
def logout():
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for("auth.login"))


@auth_bp.route("/dashboard")
@login_required
def dashboard():
    from .models import Book, Loan

    books_count = Book.query.count()
    borrowed_count = Loan.query.filter_by(status="checked_out").count()

    conn = get_auth_connection()
    users_count = conn.execute("SELECT COUNT(*) AS total FROM user").fetchone()["total"]
    conn.close()

    return render_template(
        "dashboard.html",
        books_count=books_count,
        users_count=users_count,
        borrowed_count=borrowed_count
    )