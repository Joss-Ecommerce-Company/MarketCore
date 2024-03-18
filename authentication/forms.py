from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, BooleanField
from wtforms.validators import  DataRequired, Email, EqualTo, Length, ValidationError
from authentication.models import User

"""
Authentication Forms

This module defines FlaskForm subclasses for user registration and login.
Each form includes fields for collecting user input, along with validators
to ensure the input meets certain criteria.

Forms:
    - RegistrationForm: Form for user registration, including fields for username,
      email, password, and confirm password. Provides validators for each field
      to ensure valid input.
    - LoginForm: Form for user login, including fields for email, password, and
      remember me checkbox. Provides validators for email and password fields.

"""

class RegistrationForm(FlaskForm):
    username = StringField("username", validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField("Email", validators=[DataRequired(), Email()])
    password = PasswordField("Password", validators=[DataRequired(), Length(min=8)])
    confirm_password = PasswordField("Confirm Password", validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField("Sign Up")

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user:
            raise ValidationError("This username is taken. Please choose a different username")

class LoginForm(FlaskForm):
    email = StringField("EMAIL", validators=[DataRequired(), Email()])
    password = PasswordField("Passowrd", validators=[DataRequired()])
    remember = BooleanField("Remember")
    submit = SubmitField("Login")

