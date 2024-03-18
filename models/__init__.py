'''Creating a database that store the user information when registering '''
from flask_sqlalchemy import SQLAlchemy
from .usermodel import User
db = SQLAlchemy()
