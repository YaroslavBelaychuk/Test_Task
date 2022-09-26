from flask import url_for, render_template, flash
from flask_login import login_user
from werkzeug.utils import redirect

from . import auth
from .forms import RegisterForm, LoginForm
from .utils import create_user
from ..models.user import User


@auth.route("/register", methods=["GET", "POST", ])
def register():
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            create_user(form.login.data, form.password.data)
        except:
            flash("Too short login_manager", "warning")
        return redirect(url_for("auth.register"))
    return render_template("register.html", form=form)


@auth.route("/login_manager", methods=["GET", "POST", ])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        u = User.query.filter(User.login == form.login.data).first()
        if u and u.check_pass(form.password.data):
            login_user(u)
            return redirect(url_for("main.home"))

        flash("Not found", "danger")
    return render_template("login.html", form=form)
