#!/usr/bin/env python3
from flask import flash, url_for, render_template
from werkzeug.utils import redirect

from api.v1.authentication.forms import RegistrationForm
from db import db
from api.v1.views import app_views
from models import User


@app_views.route('/register', methods=['GET', 'POST'])
def register():
    """
    Register route for new users.

    If the form data is valid, creates a new user and redirects to the index page.
    Otherwise, renders the registration form template.

    Returns:
        Redirect: Redirects to the index page upon successful registration.
        Rendered Template: Renders the registration form template.
    """
    form = RegistrationForm()
    if form.validate_on_submit():
        # Create a new user based on the form data
        user = User(username=form.username.data, email=form.email.data)
        user.set_password(form.password.data)
        db.session.add(user)
        db.session.commit()
        flash('You have successfully registered!', 'success')
        return redirect(url_for('main.index'))
    return render_template('register.html', form=form)
