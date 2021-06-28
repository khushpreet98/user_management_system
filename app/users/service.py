from app import db
from typing import List
from .model import User
from .interface import user_interface
from sqlalchemy_filters import apply_filters
import json


class user_service:


    @staticmethod
    def create(new_attrs: user_interface) -> User:
        new_user = User(first_name=new_attrs["first_name"], last_name=new_attrs["last_name"],full_name=new_attrs["full_name"],
        salary=new_attrs["salary"], address=new_attrs["address"])
        db.session.add(new_user)
        db.session.commit()
        return new_user


    @staticmethod
    def get_all(filters) -> List[User]:
        f_query = db.session.query(User)
        # add filters from list of filter
        if len(filters) > 0:
            f_query = apply_filters(f_query, filters)
        return f_query.all()

    @staticmethod
    def get_by_name(first_name:str) -> List[User]:
        return User.query.filter(User.first_name == first_name).all()


    @staticmethod
    def get_by_id(id: int) -> User:
        return User.query.get(id)


    @staticmethod
    def delete_by_id(id: int) -> List[int]:

        users = User.query.filter(User.id == id).first()
        if not users:
            return []
        db.session.delete(users)
        db.session.commit()
        return [id]

