#!/usr/bin/env python3
from flask import flash, url_for, render_template, session
from werkzeug.utils import redirect

from api.v1.views import app_views


@app_views.route("/logout")
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
