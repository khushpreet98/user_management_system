from datetime import datetime
import pandas as pd
import numpy as np
from flask_script import Command

from app import db




"""def seed_things():
    classes = []
    for klass in classes:
        seed_thing(klass)


def seed_thing(cls):
    things = [
        {"name": "Pizza Slicer", "purpose": "Cut delicious pizza"},
        {"name": "Rolling Pin", "purpose": "Roll delicious pizza"},
        {"name": "Pizza Oven", "purpose": "Bake delicious pizza"},
    ]
    db.session.bulk_insert_mappings(cls, things)"""


class SeedCommand(Command):
    """ Seed the DB."""

    def run(self):
            db.drop_all()
            db.create_all()
            # seed_things()
            db.session.commit()
            print("DB successfully seeded.")
