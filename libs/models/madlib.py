# Anthony
from models.__init__ import CURSOR, CONN


class MadLib:
    all = {}

    def __init__(self, author_words_list, author, template):
        self.author_words_list = author_words_list
        self.author = author
        self.template = template

    def __repr__(self):
        return f"<MadLib {self.id}: {self.author_words_list}, {self.author}, {self.template}>"

    @property
    def author_words_list(self):
        return self._author_words_list

    @author_words_list.setter
    def author_words_list(self, author_words_list):
        if not isinstance(author_words_list, list):
            raise TypeError("author_words_list must be a list")
        elif not all(isinstance(word, str) for word in author_words_list):
            raise TypeError("author_words_list must be a list of strings")
        else:
            self._author_words_list = author_words_list

    @property
    def author(self):
        return self._author

    @author.setter
    def author(self, author):
        from models.author import Author

        if not isinstance(author, Author):
            raise TypeError("author must be an Author instance")
        else:
            self._author = author

    @property
    def template(self):
        return self._template

    @template.setter
    def template(self, template):
        from models.template import Template

        if not isinstance(template, Template):
            raise TypeError("template must be a Template instance")
        else:
            self._template = template

    @classmethod
    def create_table(cls):
        """Create a new table to persist the attributes of MadLib instances"""
        sql = """
            CREATE TABLE IF NOT EXISTS madlibs (
            id INTEGER PRIMARY KEY,
            author_words_list BLOB,
            author FOREIGNKEY,
            template FOREIGNKEY)
        """
        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        """Drop the table that persists MadLib instances"""
        sql = """
            DROP TABLE IF EXISTS madlibs;
        """
        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        """Save a new MadLib to the database"""
        sql = """
            INSERT INTO madlibs (author_words_list, author, template)
            VALUES (?, ?, ?)
        """
        CURSOR.execute(sql, (self.author_words_list, self.author, self.template))
        CONN.commit()
        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, author_words_list, author, template):
        """Initialize a new MadLib instance and save the object to the database"""
        madlib = cls(author_words_list, author, template)
        madlib.save()
        return madlib

    def update(self):
        """Update the table row corresponding to the current MadLib instance."""
        sql = """
            UPDATE madlibs
            SET author_words_list = ?, author = ?, template = ?
            WHERE id = ?
        """
        CURSOR.execute(
            sql, (self.author_words_list, self.author, self.template, self.id)
        )
        CONN.commit()

    def delete(self):
        """Delete the table row corresponding to the current MadLib instance,
        delete the dictionary entry, and reassign id attribute"""
        sql = """
            DELETE FROM madlibs
            WHERE id = ?
        """
        CURSOR.execute(sql, (self.id,))
        CONN.commit()
        # Delete the dictionary entry using id as the key
        del type(self).all[self.id]
        # Set the id to None
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a MadLib object having the attribute values from the table row."""
        # Check the dictionary for an existing instance using the row's primary key
        madlib = cls.all.get(row[0])
        if madlib:
            # ensure attributes match row values in case local instance was modified
            madlib.author_word_list = row[1]
            madlib.author = row[2]
            madlib.template = row[3]
        else:
            # not in dictionary, create new instance and add to dictionary
            madlib = cls(row[1], row[2], row[3])
            madlib.id = row[0]
            cls.all[madlib.id] = madlib
        return madlib

    @classmethod
    def get_all(cls):
        """Return a list containing a MadLib object per row in the table"""
        sql = """
            SELECT *
            FROM madlibs
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def find_by_id(cls, id):
        """Return a MadLib object corresponding to the table row matching the specified primary key"""
        sql = """
            SELECT *
            FROM madlibs
            WHERE id = ?
        """
        row = CURSOR.execute(sql, (id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_author_id(cls, author_id):
        """Return a MadLib object corresponding to first table row matching specified author_id"""
        sql = """
            SELECT *
            FROM madlibs
            WHERE author = ?
        """
        row = CURSOR.execute(sql, (author_id,)).fetchone()
        return cls.instance_from_db(row) if row else None

    @classmethod
    def find_by_template_id(cls, template_id):
        """Return a MadLib object corresponding to first table row matching specified template_id"""
        sql = """
            SELECT *
            FROM madlibs
            WHERE template = ?
        """
        row = CURSOR.execute(sql, (template_id,)).fetchone()
        return cls.instance_from_db(row) if row else None
