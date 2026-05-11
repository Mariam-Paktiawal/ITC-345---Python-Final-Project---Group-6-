import os


BASE_DIR = os.path.abspath(os.path.dirname(__file__))


class Config:
    SECRET_KEY = "library-secret-key"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + os.path.join(BASE_DIR, "instance", "library.db")
    SQLALCHEMY_TRACK_MODIFICATIONS = False

    # second database used only for authentication
    AUTH_DB_PATH = os.path.join(BASE_DIR, "auth", "instance", "library.db")