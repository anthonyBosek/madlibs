from models.__init__ import CURSOR, CONN
from models.madlib import MadLib

class Template:
    all = {}
    def __init__(self, category, title, text, pos_list):
        self.category = category
        self.title = title
        self.text = text
        self.pos_list = pos_list
        
    @property
    def catagorty(self):
        return self._category
    
    @catagorty.setter
    def category(self, category):
        if not isinstance(category, str):
            raise TypeError("Category must be of type string.")
        elif not len(category) > 1:
            raise TypeError("Category must be more than 1 character.")
        elif hasattr(self, "category"):
            raise ArithmeticError("Category cannont be changed after initialization")
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
            raise ArithmeticError("Title cannont be changed after initialization")
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
            raise ArithmeticError("Text cannont be changed after initialization")
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
            raise ArithmeticError("Part of speech list cannont be changed after initialization")
        else:
            self._pos_list = pos_list
            
    def madlibs(self):
        return [madlib for madlib in MadLib.all if madlib.template is self]  
    
    
    
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
        
        CURSOR.execute(sql, (self.category, self.title, self.text, self.pos_list, self.id))
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
    
