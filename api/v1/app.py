#!/usr/bin/env python3
from flask import Flask, jsonify
from db import db
from config import Config
from flask_cors import CORS
from views import app_views
from api.v1.request_handler import handle_request
from flask_wtf.csrf import CSRFProtect

app = Flask(__name__, template_folder='../../templates')
app.config.from_object(Config)
CSRFProtect(app)
db.init_app(app)
app.register_blueprint(app_views)
CORS(app, resources={r"/api/v1/*": {"origins": "*"}})

with app.app_context():
    # Create the database tables
    db.create_all()


@app.before_request
def handle_before_request():
    return handle_request()


@app.errorhandler(403)
def forbidden(error) -> str:
    """Custom error handler for HTTP 403 Forbidden.

    Returns:
        str: JSON response with an error message.
    """
    return jsonify({"error": "Forbidden"}), 403


@app.errorhandler(401)
def unauthorized(error) -> str:
    """Custom error handler for HTTP 401 Unauthorized.

    Returns:
        str: JSON response with an error message.
    """
    return jsonify({"error": "Unauthorized"}), 401


@app.errorhandler(404)
def not_found(error) -> str:
    """Custom error handler for HTTP 404 Not Found.

    Returns:
        str: JSON response with an error message.
    """
    return jsonify({"error": "Not Found"}), 404


if __name__ == '__main__':
    app.run(debug=False)
