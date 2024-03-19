#!/usr/bin/env python3
from db import db
from models import Base
from utils import PasswordManager

import datetime
import uuid


class User(Base):
    __tablename__ = 'users'

    def get_unique_id(self):
        new_id = str(uuid.uuid4())
        while db.session.query(User).filter_by(id=new_id).first():
            new_id = str(uuid.uuid4())
        return new_id

    id = db.Column(db.String(36), primary_key=True, default=get_unique_id)
    created_at = db.Column(db.DateTime, default=datetime.datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.datetime.now, onupdate=datetime.datetime.now)
    username = db.Column(db.String(50), unique=True, nullable=False)
    email = db.Column(db.String(100), unique=True, nullable=False)
    password = db.Column(db.String(100), nullable=False)

    def __init__(self, username, email, password):
        super().__init__()
        self.username = username
        self.email = email

        salt = PasswordManager.generate_salt()
        hashedpassword = PasswordManager.hash_password(password, salt)
        self.password = hashedpassword
