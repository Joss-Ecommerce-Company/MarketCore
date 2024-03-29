#!/usr/bin/env python3
from dotenv import load_dotenv
import os

load_dotenv()


class Config:
    SQLALCHEMY_DATABASE_URI = 'sqlite:///example.db'
    SQLALCHEMY_TRACK_MODIFICATIONS = False
    PROPAGATE_EXCEPTIONS = True
    SECRET_KEY = os.getenv('SECRET_KEY')
