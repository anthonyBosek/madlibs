import sqlite3

CONN = sqlite3.connect("AAAMadLibs.db")
CURSOR = CONN.cursor()

__all__ = ["author", "madlib", "template"]
