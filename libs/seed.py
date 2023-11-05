#!/usr/bin/env python3

from models.__init__ import CONN, CURSOR
from models.author import Author
from models.madlib import MadLib
from models.template import Template


def seed_database():
    MadLib.drop_table()
    MadLib.create_table()

    author = Author("Alberto", "Vega", [])
    template = Template(
        "Adventure", "Climb a Moutain", "Test", ["verb", "noun", "adjective"]
    )
    MadLib.create(["run", "dog", "happy"], author, template)


seed_database()
print("Seeded database")
