import hashlib

from flask_login import UserMixin
from sqlalchemy.orm import validates

from app import login_manager, db


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    login = db.Column(db.String(18), unique=True, nullable=False)
    password = db.Column(db.Text, nullable=False)

    @validates("login")
    def validate_login(self, key, login) -> str:
        if len(login) > 18:
            raise ValueError("Too long")
        return login

    def check_pass(self, password: str) -> bool:
        return self.password == User.enc_string(password)

    @staticmethod
    def enc_string(password) -> str:
        return hashlib.sha256(
            password.encode("utf-8"),
        ).hexdigest()

    def set_pass(self, password: str):
        self.password = User.enc_string(password)


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))
