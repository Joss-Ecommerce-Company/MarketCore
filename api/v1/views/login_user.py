#!/usr/bin/env python3
from flask import flash, url_for, render_template, session
from werkzeug.utils import redirect

from api.v1.authentication.forms import LoginForm
from api.v1.views import app_views
from models import User


@app_views.route("/login", methods=["GET", "POST"])
def login():
    """
    Login route for existing users.

    If the form data is valid and the user exists with the correct password,
    logs the user in and redirects to the index page.
    Otherwise, renders the login form template.

    Returns:
        Redirect: Redirects to the index page upon successful login.
        Rendered Template: Renders the login form template.
    """
    form = LoginForm()
    if form.validate_on_submit():
        # Check if the user exists and the password is correct
        user = User.query.filter_by(email=form.email.data).first()
        if user and user.check_password(form.password.data):
            session['user_id'] = user.id
            if form.remember.data:
                # If remember me is checked, set a longer session expiry time
                session.permanent = True
            flash('You have successfully logged in!', 'success')
            return redirect(url_for('main.index'))
        else:
            flash('Invalid email or password. Please try again.', 'danger')
    return render_template('login.html', form=form)
