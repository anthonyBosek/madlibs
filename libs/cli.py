import subprocess
from models import *
from rich import print
from rich.console import Console
import time
import re

console = Console()
current_author = None
current_template = None


def welcome():
    subprocess.call("clear")
    console.print(read_("./libs/txts/welcome.txt"), style="magenta b")
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
    while True:
        console.print(read_("./libs/txts/categories.txt"), style="yellow b")
        all_cats = template.Template.get_all_categorys()
        i = 1
        for cat in all_cats:
            console.print(f"{i}. {cat}", style='yellow')
            i += 1
        console.print(template.Template.most_used_template(), style="blue bold")
        console.print("Select a category by number:", style="cyan underline bold")
        category = input("> ").strip()
        try:
            category_index = int(category)
            if 1 <= category_index <= len(all_cats):
                cat = all_cats[category_index - 1]
                enter_words(cat)
                break  # Exit the loop when a valid category is selected
            else:
                subprocess.call("clear")
                console.print(
                    "Invalid category number. Please select a valid category by number."
                )
        except ValueError:
            subprocess.call("clear")
            console.print("Please select a category by entering its number.")
        except IndexError:
            subprocess.call("clear")
            console.print(
                "Invalid category number. Please select a valid category by number."
            )


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
        console.print(f"Enter a {word}: ", style="white")
        author_word = input("> ").strip()
        while not author_word:
            console.print(f"Enter a {word}: ", style="white")
            author_word = input("> ").strip()
        author_words.append(author_word)
    new_madlib = madlib.MadLib.create(author_words, author_id, temp_id)
    create_madlib(new_madlib)


def create_madlib(madlib):
    new_madlib = current_template[3]
    author_words = madlib.author_words_list.split(",")
    name = current_author.first_name + " " + current_author.last_name
    new_madlib = re.sub(r"\[Author\]",name, new_madlib)
    story = re.sub(
        r"\[\d{,2}\]", lambda x: f"[yellow b]{author_words[int(x.group()[1])].strip()}[/yellow b]", new_madlib
    )
    console.print("Here's your new MadLib!", style='yellow b')
    console.print(f"{current_template[2]}",style='green b underline')
    console.print(f"{story}",style="white")
    console.print(f"Created by:{current_author.first_name + ' ' + current_author.last_name}",style="cyan")
    new_game()
    
        
def new_game():
    console.print("Enter '-new' to play again!")
    
    choice = input("").lower()
    if choice == "-new":
        select_category()
    
    
    # author name color


def help_options():
    console.print(read_("./libs/txts/help.txt"),style="white b")
    choice = input("").lower()
    if choice == "-start":
        create_author()


def exit_program():
    console.print("Thanks for stopping in. Goodbye!", style='magenta')
    exit()


def read_(file):
    with open(file, "r") as file:
        return file.read()


if __name__ == "__main__":
    welcome()
