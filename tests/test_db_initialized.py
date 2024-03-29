import unittest
from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from db import db
from models import User
import utils


class TestFlaskSQLAlchemy(unittest.TestCase):
    def setUp(self):
        self.app = Flask(__name__)
        self.app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite://'
        self.app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
        self.db = db
        db.init_app(self.app)

        self.app_context = self.app.app_context()
        self.app_context.push()

    def tearDown(self):
        self.db.session.remove()
        self.db.drop_all()
        self.app_context.pop()

    def test_db_initialized(self):
        """Test if the SQLAlchemy instance is correctly initialized."""
        self.assertIsInstance(self.db, SQLAlchemy)

    def test_create_table(self):
        """Test if a table can be created."""
        self.db.create_all()

        inspector = self.db.inspect(self.db.engine)
        table_names = inspector.get_table_names()
        self.assertIn('users', [t.lower() for t in table_names])

    def test_insert_data(self):
        """Test if data can be inserted into a table."""
        self.db.create_all()

        user = User('testuser', 'demo@demo.com', utils.PasswordManager.hash_password('testpassword'))
        self.db.session.add(user)
        self.db.session.commit()

        self.assertEqual(User.query.count(), 1)
        self.assertEqual(User.query.first().username, 'testuser')
