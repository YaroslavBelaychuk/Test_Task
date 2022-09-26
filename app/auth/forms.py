from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, DataRequired, EqualTo, ValidationError

from app.models.user import User


class RegisterForm(FlaskForm):
    login = StringField("Login", validators=[Length(4, 20), ])
    password = PasswordField("Password", validators=[DataRequired()])
    password2 = PasswordField("Repeat password", validators=[EqualTo('password'), ], )
    submit = SubmitField("Register")

    def validate_login(self, login):
        user = User.query.filter(User.login == login.data).first()
        if user is not None:
            raise ValidationError("Login already exists")


class LoginForm(FlaskForm):
    login = StringField("Login", validators=[DataRequired(), ])
    password = PasswordField("Password", validators=[DataRequired(), ])
    submit = SubmitField("Sign In")


