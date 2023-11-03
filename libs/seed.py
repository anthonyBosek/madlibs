#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.author import Author
from models.madlib import Madlib
from models.template import Template


def seed_database():
    pass


seed_database()
print("Seeded database")
