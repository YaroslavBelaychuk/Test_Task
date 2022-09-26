from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from wtforms.csrf.core import CSRF

from config import config


csrf = CSRF()
login_manager = LoginManager()
db = SQLAlchemy()


def create_app(config_name: str = "default") -> Flask:
    app = Flask(__name__)
    app.config.from_object(config[config_name])

    login_manager.login_view = "auth.login"
    login_manager.init_app(app)
    db.init_app(app)

    from .main import main as main_bp
    app.register_blueprint(main_bp)

    from .auth import auth as auth_bp
    app.register_blueprint(auth_bp)

    return app


from app.models import *
