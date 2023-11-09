from models.__init__ import CURSOR, CONN


class Author:
    all = {}

    def __init__(self, first_name, last_name):
        self.first_name = first_name
        self.last_name = last_name

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

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS authors (
            id INTEGER PRIMARY KEY,
            first_name TEXT,
            last_name TEXT)
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

    @classmethod
    def create(cls, first_name, last_name):
        new_author = cls(first_name, last_name)
        new_author.save()
        return new_author

    def save(self):
        CURSOR.execute(
            """
                INSERT INTO authors(first_name, last_name)
                VALUES(?, ?)
            """,
            (self.first_name, self.last_name),
        )
        CONN.commit()
        self.id = CURSOR.lastrowid
        Author.all[self.id] = self

    # class method to verify if author exists
    @classmethod
    def author_exists(cls, first_name, last_name):
        sql = """
            SELECT * FROM authors
            WHERE first_name = ? AND last_name = ?
        """
        CURSOR.execute(sql, (first_name, last_name))
        row = CURSOR.fetchone()
        if row:
            return True
        else:
            return False

    # class method to grab author by first and last name
    @classmethod
    def get_author_by_name(cls, first_name, last_name):
        sql = """
            SELECT * FROM authors
            WHERE first_name = ? AND last_name = ?
        """
        CURSOR.execute(sql, (first_name, last_name))
        row = CURSOR.fetchone()
        if row:
            return row
        else:
            return None

    # class method to delete author by id
    @classmethod
    def delete_author_by_id(cls, id):
        sql = """
            DELETE FROM authors
            WHERE id = ?
        """
        CURSOR.execute(sql, (id,))
        CONN.commit()
        # del cls.all[id]

    # class method to randomly grab a completed madlib by author id
    @classmethod
    def get_random_madlib(cls, id):
        sql = """
            SELECT * FROM madlibs
            WHERE author_id = ?
            ORDER BY RANDOM()
            LIMIT 1
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        if row:
            return row
        else:
            return None
