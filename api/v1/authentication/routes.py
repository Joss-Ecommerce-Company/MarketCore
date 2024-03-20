from flask import Blueprint, render_template, redirect, url_for, session, flash
from .forms import LoginForm, RegistrationForm
from models import db, User

auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
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


@auth.route("/login", methods=["GET", "POST"])
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


@auth.route("/logout")
def logout():
    """
    Logout route for users.

    Clears the session and redirects to the login page.

    Returns:
        Redirect: Redirects to the login page.
    """
    session.clear()
    flash('You have been logged out.', 'info')
    return redirect(url_for("auth.login"))
