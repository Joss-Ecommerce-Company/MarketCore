from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

'''Creating a database that store the user information when registering '''
class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unque=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)