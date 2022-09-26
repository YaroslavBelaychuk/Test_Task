from app import db
from app.models.user import User


def create_user(login, password):
    u = User(login=login)
    u.set_pass(password)
    db.session.add(u)
    db.session.commit()
    return u
