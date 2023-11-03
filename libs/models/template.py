# Austin
class Template:
    all = []

    def __init__(self, category, title, text, pos_list):
        self.category = category
        self.title = title
        self.text = text
        self.pos_list = pos_list
        type(self).all.append(self)
