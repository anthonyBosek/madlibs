import re
import subprocess
from models import *
from rich import print
from rich.console import Console
import time


console = Console()
current_author = None
current_template = None


def welcome():
    subprocess.call("clear")
    console.print(read_("./libs/txts/welcome.txt"), style="magenta")
    choice = input("> ").lower()
    if choice == "-exit":
        exit_program()
    elif choice == "-help":
        help_options()
    elif choice == "-start":
        create_author()
    else:
        print("Invalid choice. Please enter '-exit', '-help', or '-start'.")
        time.sleep(2.5)
        welcome()


def create_author():
    global current_author
    subprocess.call("clear")

    # Get the first name and validate it
    console.print("Enter your first name:", style="cyan underline bold")
    first_name = input("> ").strip()
    while not first_name:
        subprocess.call("clear")
        console.print(
            "First name cannot be blank. Please enter your first name.",
            style="cyan underline bold",
        )
        first_name = input("> ").strip()

    # Get the last name and validate it
    console.print("Enter your last name:", style="cyan underline bold")
    last_name = input("> ").strip()
    while not last_name:
        subprocess.call("clear")
        console.print(
            "Last name cannot be blank. Please enter your last name.",
            style="cyan underline bold",
        )
        last_name = input("> ").strip()

    subprocess.call("clear")
    console.print(f"Hello {first_name} {last_name}", style="cyan underline bold")
    print()
    current_author = author.Author.create(first_name, last_name)
    select_category()


def select_category():
    console.print(read_("./libs/txts/categories.txt"), style="yellow")
    all_cats = template.Template.get_all_categorys()
    i = 1
    for cat in all_cats:
        print(f"{i}. {cat}")
        i += 1
    category = input("> ").strip()
    while not category == category:
        console.print("Please select a category by number!")
        category = input("> ").strip()
    cat = all_cats[int(category) - 1]
    enter_words(cat)


def enter_words(category):
    global current_template
    subprocess.call("clear")
    print(category)
    temp = template.Template.get_random_template_by_category(template, category)
    current_template = temp
    author_words = []
    author_id = current_author.id
    temp_id = temp[0]
    for word in temp[4].split(","):
        if re.search("^[aeiou]", word.strip(), re.IGNORECASE):
            print("Enter an", word.strip(), ":")
        else:
            print("Enter a", word.strip(), ":")
        # console.print(f"Enter a {word.strip()}: ", style="white")
        word = input("> ")
        author_words.append(word)
    new_madlib = madlib.MadLib.create(author_words, author_id, temp_id)
    create_madlib(new_madlib)


def create_madlib(madlib):
    new_madlib = current_template[3]
    author_words = madlib.author_words_list.split(",")
    name = current_author.first_name + " " + current_author.last_name
    new_madlib = re.sub(r"\[Author\]", name, new_madlib)
    story = re.sub(
        r"\[\d+\]", lambda x: author_words[int(x.group()[1])].strip(), new_madlib
    )
    print(story)


def help_options():
    subprocess.call("clear")
    print(read_("./libs/txts/help.txt"))
    input("Press enter to continue...")
    welcome()


def exit_program():
    print("Thanks for stopping in. Goodbye!")
    exit()


def read_(file):
    with open(file, "r") as file:
        return file.read()


if __name__ == "__main__":
    welcome()
