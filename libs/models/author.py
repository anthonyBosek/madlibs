from models.__init__ import CURSOR, CONN


class Author:
    all = []

    def __init__(self, first_name, last_name, saved_madlibs):
        self._first_name = None
        self._last_name = None
        self._saved_madlibs = None

        self.first_name = first_name
        self.last_name = last_name
        self.saved_madlibs = saved_madlibs
        type(self).all.append(self)

    @property
    def first_name(self):
        return self._first_name

    @first_name.setter
    def first_name(self, first_name):
        if not isinstance(first_name, str) or not 1 <= len(first_name) <= 15:
            raise TypeError(
                "First name must be a string between 1 and 15 characters long."
            )
        else:
            self._first_name = first_name

    @property
    def last_name(self):
        return self._last_name

    @last_name.setter
    def last_name(self, last_name):
        if not isinstance(last_name, str) or not 1 <= len(last_name) <= 15:
            raise TypeError(
                "Last name must be a string between 1 and 15 characters long."
            )
        else:
            self._last_name = last_name

    @property
    def saved_madlibs(self):
        return self._saved_madlibs

    @saved_madlibs.setter
    def saved_madlibs(self, madlibs):
        if not isinstance(madlibs, str):  # ? type madlibs class or list?
            raise TypeError("Madlib must be a list")
        else:
            self._saved_madlibs = madlibs

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT,
            saved_madlibs TEXT)
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS authors;
        """

        CURSOR.execute(sql)
        CONN.commit()
