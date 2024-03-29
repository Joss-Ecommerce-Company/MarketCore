#!/usr/bin/env python3

from api.v1 import app
from flask import jsonify, request


def handle_request():
    """Handles request authentication and authorization.

    This function is executed before processing each incoming request.
    It checks if authentication and authorization are required for the
    requested path and validates the user's credentials.

    Returns:
        None: If the request is valid and authorized.
        HTTP 401 Unauthorized: If the request lacks proper authentication.
        HTTP 403 Forbidden: If the user does not have permission to
        access the resource.
    """
    print(f"befor request handled{request.full_path}")
