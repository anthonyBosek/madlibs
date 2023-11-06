#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.author import Author
from models.madlib import MadLib
from models.template import Template


def seed_database():
    Author.drop_table()
    Author.create_table()
    MadLib.drop_table()
    MadLib.create_table()
    Template.drop_table()
    Template.create_table()


seed_database()
print("Seeded database")
