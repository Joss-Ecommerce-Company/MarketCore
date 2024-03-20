#!/usr/bin/env python3
from flask import Flask
from db import db
from config import Config

app = Flask(__name__)
app.config.from_object(Config)
db.init_app(app)

with app.app_context():
    # Create the database tables
    db.create_all()

if __name__ == '__main__':
    app.run(debug=True)
