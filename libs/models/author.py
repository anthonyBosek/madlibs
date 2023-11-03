class Author:
    all = []
    def __init__(self, first_name, last_name, saved_madlibs):
        self.first_name = first_name
        self.last_name = last_name
        self.saved_madlibs = saved_madlibs
        type(self).all.append(self)