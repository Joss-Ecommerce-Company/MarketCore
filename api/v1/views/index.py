#!/usr/bin/env python3

from api.v1.views import app_views
from flask import abort, jsonify


@app_views.route('/forbidden', strict_slashes=False)
def forbidden() -> str:
    """
    Raise a forbidden error.

    Returns:
        str: JSON response indicating a forbidden error.
    """
    abort(403)


@app_views.route('/unauthorized', strict_slashes=False)
def unauthorized() -> str:
    """
    Raise an unauthorized error.

    Returns:
        str: JSON response indicating an unauthorized error.
    """
    abort(401)


@app_views.route('/not_found', strict_slashes=False)
def not_found() -> str:
    """
    Raise a not found error.

    Returns:
        str: JSON response indicating a not found error.
    """
    abort(404)


@app_views.route('/', methods=['GET'], strict_slashes=False)
def status() -> str:
    """
    GET /api/v1/

    Returns:
        str: JSON response with the status of the API.
    """
    return jsonify({"status": "OK"})
