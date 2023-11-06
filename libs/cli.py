import subprocess
from models import *
from rich import print
from rich.console import Console


console = Console()

def welcome():
    console.print(read_("./libs/txts/welcome.txt"),style='magenta')
    choice = input("> ")
    if choice == "-exit":
        exit_program()
    elif choice == "-help":
        help_options()
    else:
        create_author()


def create_author():
    subprocess.call("clear")
    console.print("Enter your first name: ",style='cyan underline bold')
    first_name = input("> ")
    console.print("Enter your last name: ",style='cyan underline bold')
    last_name = input("> ")
    subprocess.call("clear")
    console.print(f"Hello {first_name} {last_name}",style='cyan underline bold')
    print()
    select_category()


def select_category():
    console.print(read_("./libs/txts/categories.txt"),style='yellow')
    category = input("> ")
    subprocess.call("clear")
    temp = ["adjective", "noun", "verb", "adverb"]
    # temp = template.Template.select_random(category)
    # randomly select template based on category
    enter_words(temp)


def enter_words(temp):
    for word in temp:
        # for word in temp.pos_list:
        console.print(f"Enter a {word}: ",style='white')
        word = input("> ")


def create_madlib():
    pass


def help_options():
    print(read_("./libs/txts/help.txt"))


def exit_program():
    print("Thanks for stopping in. Goodbye!")
    exit()


def read_(file):
    with open(file, "r") as file:
        return file.read()



if __name__ == "__main__":
    welcome()
