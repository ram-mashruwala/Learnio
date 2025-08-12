import sqlalchemy as sa
from app.extensions import db
from app.models import User
from flask_wtf import FlaskForm
from wtforms import BooleanField, EmailField, PasswordField, StringField, SubmitField, ValidationError
from wtforms.validators import DataRequired, Email, EqualTo, Length

class LoginForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired()])
    password = PasswordField(label="Password", validators=[DataRequired()])
    remember_me = BooleanField(label="Remember Me")
    submit_button = SubmitField(label="Submit")

class RegisterForm(FlaskForm):
    username = StringField(label="Username", validators=[DataRequired(), Length(30)])
    email = EmailField(label="Email", validators=[DataRequired(), Email(message="Must be a valid Email Address")])
    password = PasswordField(label="Password", validators=[DataRequired()])
    repeat_password = PasswordField(label="Repeat Password", validators=[DataRequired(), EqualTo("password", message="Passwords must Match!")])
    terms_and_conditions = BooleanField(label="Terms and Conditions", validators=[DataRequired()])
    register_button = SubmitField(label="Register")

    def validate_username(self, username):
        user = db.session.scalar(sa.select(User).where(User.username == username.data))
        if user:
            raise ValidationError("Username is already taken!")

    def validate_email(self, email):
        email = db.session.scalar(sa.select(User).where(User.email == email.data))
        if email:
            raise ValidationError("Email Already Taken!")
