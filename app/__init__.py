from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def create_app():

    app = Flask(__name__)

    app.config.from_object("config.Config")

    db.init_app(app)

    with app.app_context():

        from .models import User, Book, Loan
        from .books import books

        app.register_blueprint(books)

        db.create_all()

    @app.route("/")
    def home():
        return "Library Management System is Running!"

    return app