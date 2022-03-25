from sqlalchemy import Integer, Column, String, DateTime
from app import db
from datetime import datetime
from .interface import UserInterface

class User(db.Model):

    __tablename__ = "users"
    id = Column(Integer(), primary_key=True)
    first_name = Column(String(100))
    last_name = Column(String(100))
    full_name = Column(String(100))
    salary = Column(Integer())
    address = Column(String(100))
    created_at = Column(DateTime, default = datetime.utcnow())

    def update(self, changes: UserInterface):
        for key, val in changes.items():
            setattr(self, key, val)
        return self

