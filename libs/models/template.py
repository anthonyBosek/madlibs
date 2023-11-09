from models.__init__ import CURSOR, CONN
from models.madlib import MadLib
import sqlite3
import random


class Template:
    all = {}

    def __init__(self, category, title, text, pos_list):
        self.category = category
        self.title = title
        self.text = text
        self.pos_list = pos_list

    @property
    def category(self):
        return self._category

    @category.setter
    def category(self, category):
        if not isinstance(category, str):
            raise TypeError("Category must be of type string.")
        elif not len(category) > 1:
            raise TypeError("Category must be more than 1 character.")
        elif hasattr(self, "category"):
            raise ArithmeticError("Category cannot be changed after initialization")
        else:
            self._category = category

    @property
    def title(self):
        return self._title

    @title.setter
    def title(self, title):
        if not isinstance(title, str):
            raise TypeError("Title must be of type string.")
        elif not len(title) > 1:
            raise TypeError("Title must be more than 1 character.")
        elif hasattr(self, "title"):
            raise ArithmeticError("Title cannot be changed after initialization")
        else:
            self._title = title

    @property
    def text(self):
        return self._text

    @text.setter
    def text(self, text):
        if not isinstance(text, str):
            raise TypeError("Text must be of type string.")
        elif not len(text) > 10:
            raise TypeError("Text must be more than 10 character.")
        elif hasattr(self, "text"):
            raise ArithmeticError("Text cannot be changed after initialization")
        else:
            self._text = text

    @property
    def pos_list(self):
        return self._pos_list

    @pos_list.setter
    def pos_list(self, pos_list):
        if not isinstance(pos_list, str):
            raise TypeError("Part of speech list must be of type list.")
        elif not len(pos_list) >= 1:
            raise TypeError("Part of speech list must be more than 1 character.")
        elif hasattr(self, "pos_list"):
            raise ArithmeticError(
                "Part of speech list cannot be changed after initialization"
            )
        else:
            self._pos_list = pos_list

    def all_madlibs(self):
        # for id, madlib in MadLib.all.items():
        #     print(madlib.template_id)
        return [
            madlib for id, madlib in MadLib.all.items() if madlib.template_id is self.id
        ]
        # return [madlib for madlib in MadLib.all if madlib[3] is self.id]

    @classmethod
    def create_table(cls):
        sql = """
            CREATE TABLE IF NOT EXISTS templates (
            id INTEGER PRIMARY KEY,
            category TEXT,
            title TEXT,
            text TEXT,
            pos_list LIST)
        """

        CURSOR.execute(sql)
        CONN.commit()

    @classmethod
    def drop_table(cls):
        sql = """
            DROP TABLE IF EXISTS templates;
        """

        CURSOR.execute(sql)
        CONN.commit()

    def save(self):
        sql = """
            INSERT INTO templates (category, title, text, pos_list)
            VALUES (?, ?, ?, ?)
        """

        CURSOR.execute(sql, (self.category, self.title, self.text, self.pos_list))
        CONN.commit()

        self.id = CURSOR.lastrowid
        type(self).all[self.id] = self

    @classmethod
    def create(cls, category, title, text, pos_list):
        pos_list = ", ".join(pos_list)
        template = cls(category, title, text, pos_list)
        template.save()
        return template

    def update(self):
        sql = """
            UPDATE templates
            SET category = ?, title = ?, text = ?, pos_list = ?
            WHERE id = ?
        """

        CURSOR.execute(
            sql, (self.category, self.title, self.text, self.pos_list, self.id)
        )
        CONN.commit()

    def delete(self):
        sql = """
            DELETE FROM templates
            WHERE id = ?
        """

        CURSOR.execute(sql, (self.id,))
        CONN.commit()

        del type(self).all[self.id]
        self.id = None

    @classmethod
    def instance_from_db(cls, row):
        """Return a MadLib object having the attribute values from the table row."""
        # Check the dictionary for an existing instance using the row's primary key
        template = cls.all.get(row[0])
        if template:
            # ensure attributes match row values in case local instance was modified
            template.category = row[1]
            template.title = row[2]
            template.text = row[3]
            template.pos_list = row[4]
        else:
            # not in dictionary, create new instance and add to dictionary
            template = cls(row[1], row[2], row[3], row[4])
            template.id = row[0]
            cls.all[template.id] = template
        return template

    @classmethod
    def get_all(cls):
        """Return a list containing a MadLib object per row in the table"""
        sql = """
            SELECT *
            FROM templates
        """
        rows = CURSOR.execute(sql).fetchall()
        return [cls.instance_from_db(row) for row in rows]

    @classmethod
    def get_all_categorys(cls, category=None):
        categories = []

        # Define the SQL query to select distinct categories
        sql = """
            SELECT DISTINCT category
            FROM templates
        """

        if category is not None:
            # If a specific category is provided, filter the query
            sql += " WHERE category = ?"

        # Connect to the database and execute the query
        connection = sqlite3.connect("AAAMadLibs.db")  # Replace with your database name
        try:
            cursor = connection.cursor()
            if category is not None:
                cursor.execute(sql, (category,))
            else:
                cursor.execute(sql)

            rows = cursor.fetchall()

            # Extract categories from the results
            for row in rows:
                categories.append(row[0])

        except sqlite3.Error as e:
            print(f"Error: {e}")
        finally:
            connection.close()

        return categories

    # ----------  GETS THE RANDOMS TEMPLATE BY CATEGORY  -------
    def get_random_template_by_category(cls, category):
        connection = sqlite3.connect("AAAMadLibs.db")

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM templates WHERE category = ?", (category,))
            templates = cursor.fetchall()

            if templates:
                random_template = random.choice(templates)
                return random_template
            else:
                print(f"No templates found in the '{category}' category.")
                return None

        except sqlite3.Error as e:
            print(f"Error: {e}")
            return None

        finally:
            connection.close()

    # ----------  GETS THE RANDOMS TEMPLATE TITLE  -------
    def get_random_template_by_category_title(cls, category):
        connection = sqlite3.connect("AAAMadLibs.db")

        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM templates WHERE category = ?", (category,))
            templates = cursor.fetchall()

            if templates:
                random_template = random.choice(templates)
                return random_template[2]
            else:
                print(f"No templates found in the '{category}' category.")
                return None

        except sqlite3.Error as e:
            print(f"Error: {e}")
            return None

        finally:
            connection.close()

    # ----------  GETS THE RANDOMS TEMPLATE TEXT -------
    def get_random_template_by_category_text(cls, category):
        connection = sqlite3.connect("AAAMadLibs.db")
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM templates WHERE category = ?", (category,))
            templates = cursor.fetchall()

            if templates:
                random_template = random.choice(templates)
                return random_template[3]
            else:
                print(f"No templates found in the '{category}' category.")
                return None

        except sqlite3.Error as e:
            print(f"Error: {e}")
            return None

        finally:
            connection.close()

    # ----------  GETS THE RANDOMS TEMPLATE PARTS OF SPEECH  -------
    def get_random_template_by_category_pos_list(cls, category):
        connection = sqlite3.connect("AAAMadLibs.db")
        try:
            cursor = connection.cursor()
            cursor.execute("SELECT * FROM templates WHERE category = ?", (category,))
            templates = cursor.fetchall()

            if templates:
                random_template = random.choice(templates)
                pos_list = random_template[4].split(", ")
                return pos_list
            else:
                print(f"No templates found in the '{category}' category.")
                return None

        except sqlite3.Error as e:
            print(f"Error: {e}")
            return None

        finally:
            connection.close()

    def authors(self):
        return [madlib.author_id for madlib in self.all_madlibs()]

    # most used template by number of authors
    @classmethod
    def most_used_template(cls):
        sql = """
            SELECT templates.category, templates.title, COUNT(madlibs.author_id) AS count
            FROM templates
            JOIN madlibs ON templates.id = madlibs.template_id
            GROUP BY templates.title
            ORDER BY count DESC
            LIMIT 1
        """
        row = CURSOR.execute(sql).fetchone()
        return f"*{row[0].title()} has the most popular template - '{row[1].title()}'."
        # return f"{row[1].title()} is the most used template with {row[2]} authors. It is available in the {row[0].title()} category."

    # class method to grab template by id
    @classmethod
    def get_template_by_id(cls, id):
        sql = """
            SELECT * FROM templates
            WHERE id = ?
        """
        CURSOR.execute(sql, (id,))
        row = CURSOR.fetchone()
        if row:
            return row
        else:
            return None
