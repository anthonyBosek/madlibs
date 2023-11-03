# Anthony
from models.__init__ import CURSOR, CONN


class MadLib:
    all = {}

    def __init__(self, author_words_list, author, template):
        self.author_words_list = author_words_list
        self.author = author
        self.template = template

    def save(self):
        """Save a new madlib to the database"""
        sql = """
            INSERT INTO madlibs (author_words_list, author, template)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.author_words_list, self.author, self.template))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self
