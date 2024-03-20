#!/usr/bin/env python3
from datetime import datetime
from db import db


class Base(db.Model):
    """
    Base class for all models.
    """
    __abstract__ = True

    created_at = db.Column(db.DateTime, default=datetime.now)
    updated_at = db.Column(db.DateTime, default=datetime.now, onupdate=datetime.now)

    def save(self):
        """
        Save the instance to the database and update the updated_at attribute.
        """
        db.session.add(self)
        db.session.commit()

    def to_dict(self):
        """
        Return a dictionary representation of the instance.
        """
        dictionary = self.__dict__.copy()
        dictionary["__class__"] = self.__class__.__name__
        return dictionary
