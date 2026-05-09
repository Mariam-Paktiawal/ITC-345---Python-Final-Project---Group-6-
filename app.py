from flask import Flask, redirect, render_template, url_for
from flask_login import LoginManager, current_user, login_required

from auth import auth_bp
from models import User, db

app = Flask(__name__)

app.config["SECRET_KEY"] = "your_secret_key_here"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///library.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False

db.init_app(app)

login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "auth.login"
login_manager.login_message_category = "warning"


@login_manager.user_loader
def load_user(user_id):
    return db.session.get(User, int(user_id))


app.register_blueprint(auth_bp)


@app.route("/")
def home():
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    return render_template("login.html")


@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html")


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
