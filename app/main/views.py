from flask import render_template
from flask_login import login_required

from . import main
from .utils import get_solve
from .. import db


@main.get("/")
def home():
    return render_template("home.html")


@main.get("/secret-<type>")
# @login_required
def secret(type):
    return render_template("secret.html", solve=get_solve(type))


@main.before_app_first_request
def init():
    db.create_all()
