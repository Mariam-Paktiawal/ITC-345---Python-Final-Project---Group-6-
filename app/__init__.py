from flask import Flask, render_template, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, current_user

db = SQLAlchemy()
login_manager = LoginManager()


def create_app():
    app = Flask(__name__)

    app.config.from_object("config.Config")
    app.secret_key = app.config["SECRET_KEY"]

    db.init_app(app)

    login_manager.init_app(app)
    login_manager.login_view = "auth.login"
    login_manager.login_message_category = "warning"

    from .auth import auth_bp, load_auth_user
    from .books import books

    @login_manager.user_loader
    def load_user(user_id):
        return load_auth_user(user_id)

    app.register_blueprint(auth_bp)
    app.register_blueprint(books)

    with app.app_context():
        from .models import User, Book, Loan
        db.create_all()

    @app.route("/")
    def home():
        if current_user.is_authenticated:
            return redirect(url_for("auth.dashboard"))
        return render_template("index.html")

    return app