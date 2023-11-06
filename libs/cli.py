import subprocess
from models import *


def welcome():
    subprocess.call("clear")
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
    new_auth = author.Author.create(first_name, last_name)
    select_category()


def select_category():
    # subprocess.call("clear")
    print(read_("./libs/txts/categories.txt"))
    all_cats = template.Template.get_all_categorys()
    i = 1
    for cat in all_cats:
        print(f"{i}. {cat}")
        i += 1
    category = input("> ")
    cat = all_cats[int(category) - 1]
    enter_words(cat)
    # enter_words(template.Template.random_template(all_cats[int(category) - 1]))


def enter_words(cat, temp=["noun", "verb", "adjective"]):
    subprocess.call("clear")
    print(cat)

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
