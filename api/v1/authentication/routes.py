from flask import Blueprint, render_template, redirect, url_for
from .forms import LoginForm, RegistrationForm


auth = Blueprint('auth', __name__)


@auth.route('/register', methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    # logic to create user
    if form.validate_on_submit():
        return redirect(url_for('main.index'))
    return render_template('register.html', form=form)


@auth.route("login", methods=["GET", 'POST'])
def login():
    form = LoginForm()
    # logic to login user
    if form.validate_on_submit():
        return redirect(url_for('main.index'))
    return render_template('login.html', form=form)
