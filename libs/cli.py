import subprocess
from models import *


def welcome():
    print(read_("./libs/txts/welcome.txt"))
    choice = input("> ")
    if choice == "-exit":
        exit_program()
    elif choice == "-help":
        help_options()
    else:
        create_author()


def create_author():
    subprocess.call("clear")
    print("Enter your first name: ")
    first_name = input("> ")
    print("Enter your last name: ")
    last_name = input("> ")
    subprocess.call("clear")
    print(f"Hello {first_name} {last_name}")
    print()
    select_category()


def select_category():
    print(read_("./libs/txts/categories.txt"))
    category = input("> ")
    subprocess.call("clear")
    temp = ["adjective", "noun", "verb", "adverb"]
    # temp = template.Template.select_random(category)
    # randomly select template based on category
    enter_words(temp)


def enter_words(temp):
    for word in temp:
        # for word in temp.pos_list:
        print(f"Enter a {word}: ")
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
