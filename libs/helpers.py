
from models.author import Author
from models.madlib import MadLib
from models.template import Template
from rich import print


def exit_program():
    exit()
    

def list_madlibs():
    templates = Template.get_all()
    for template in templates:
        print(template.title)

def list_categorys():
    categories = Template.get_all_categorys()
    for category in categories:
        print(category)


