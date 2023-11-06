
from models.author import Author
from models.madlib import MadLib
from models.template import Template


def exit_program():
    print("Goodbye!")
    exit()
    
def list_madlibs():
    templates = Template.get_all()
    for template in templates:
        print(template.title)
        
def list_categorys():
    categories = Template.get_all_categorys()
    for category in categories:
        print(category)
        

