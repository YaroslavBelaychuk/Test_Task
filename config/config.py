import os


file_path = os.path.abspath(os.getcwd())+"\database.db"

class Config(object):
    SECRET_KEY = os.environ.get("SECRET_KEY") or "secret"
    SQLALCHEMY_DATABASE_URI = "sqlite:///" + file_path
