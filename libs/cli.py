import re
import time
import subprocess
from rich.console import Console
from models import *

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
    if author.Author.author_exists(first_name, last_name):
        welcome_back(first_name, last_name)
    else:
        console.print(f"Hello {first_name} {last_name}", style="cyan bold")
        print()
        current_author = author.Author.create(first_name, last_name)
        select_category()


def select_category():
    while True:
        console.print("MadLib Categories", style="cyan underline b")
        all_cats = template.Template.get_all_categorys()
        i = 1
        for cat in all_cats:
            console.print(f"{i}. {cat}", style="yellow")
            i += 1
        print()
        console.print(template.Template.most_used_template(), style="blue bold")
        print()
        console.print(
            "Please select a category by number:", style="cyan underline bold"
        )
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
    author_id = (
        current_author.id if type(current_author) != tuple else current_author[0]
    )
    temp_id = temp[0]
    for word in temp[4].split(","):
        is_vowel = re.search("^[aeiou]", word.strip(), re.IGNORECASE)
        if is_vowel:
            console.print(f"Enter an [cyan]{word.strip()}[/cyan]: ")
        else:
            console.print(f"Enter a [cyan]{word.strip()}[/cyan]: ")
        author_word = input("> ").strip()
        subprocess.call("clear")
        while not author_word:
            subprocess.call("clear")
            print("please enter a word")
            if is_vowel:
                console.print(f"Enter an [cyan]{word.strip()}[/cyan]: ")
            else:
                console.print(f"Enter a [cyan]{word.strip()}[/cyan]: ")
            author_word = input("> ").strip()
        author_words.append(author_word)
    new_madlib = madlib.MadLib.create(author_words, author_id, temp_id)
    create_madlib(new_madlib)


def create_madlib(madlib):
    story = stringify_madlib(madlib, True)
    console.print("Here's your new MadLib!", style="cyan b")
    print()
    console.print(f"{current_template[2]}", style="green b underline")
    print()
    console.print(f"{story}", style="white")
    print()
    console.print(
        f"Created by: {current_author.first_name + ' ' + current_author.last_name}",
        style="cyan",
    )
    new_game()


# helper to stringify madlib
def stringify_madlib(madlib, is_new=False):
    new_madlib = (
        current_template[3]
        if is_new
        else template.Template.get_template_by_id(madlib[3])[3]
    )
    author_words = (
        madlib.author_words_list.split(",") if is_new else madlib[1].split(",")
    )
    name = (
        current_author.first_name + " " + current_author.last_name
        if is_new
        else current_author[1] + " " + current_author[2]
    )
    new_madlib = re.sub(r"\[Author\]", f"[green b]{name}[/green b]", new_madlib)
    regex = r"\d+"
    story = re.sub(
        r"\[(0|1|10|11|[2-9])\]",
        lambda x: f"[yellow b]{author_words[int(re.findall(regex, x.group())[0])].strip()}[/yellow b]",
        new_madlib,
    )
    return story


# existing author
def welcome_back(first_name, last_name):
    global current_author
    current_author = author.Author.get_author_by_name(first_name, last_name)
    console.print(f"Welcome Back {first_name} {last_name}", style="green bold")
    print()
    console.print("What would you like to do?", style="cyan underline bold")
    console.print(read_("./libs/txts/options.txt"), style="green b")
    console.print("Please enter option number:", style="cyan underline bold")
    option = input("> ").lower()
    if option == "1":
        rand = author.Author.get_random_madlib(current_author[0])
        temp = template.Template.get_template_by_id(rand[3])
        story = stringify_madlib(rand)
        subprocess.call("clear")
        console.print("Here's one of your MadLibs!", style="cyan b")
        print()
        console.print(f"{temp[2]}", style="green b underline")
        print()
        console.print(f"{story}", style="white")
        print()
        console.print(
            "Enter '-new' to create another! Or '-exit' to leave.", style="cyan"
        )
        choice = input("> ").lower()
        if choice == "-new":
            subprocess.call("clear")
            select_category()
        elif choice == "-exit":
            exit_program()
    elif option == "2":
        select_category()
    elif option == "3":
        author.Author.delete_author_by_id(current_author[0])
        console.print("Your account has been deleted.", style="red")
    elif option == "-exit":
        exit_program()
    elif option == "-help":
        help_options()
    else:
        subprocess.call("clear")
        console.print("Invalid option. Please enter a valid option number.")
        time.sleep(2.5)
        welcome_back(first_name, last_name)
    #


def new_game():
    console.print("Enter '-new' to play again! Or '-exit' to exit.", style="cyan")
    choice = input("> ").lower()
    if choice == "-new":
        subprocess.call("clear")
        select_category()
    elif choice == "-exit":
        exit_program()


def help_options():
    subprocess.call("clear")
    console.print(read_("./libs/txts/help.txt"), style="white b")
    choice = input("").lower()
    if choice == "-start":
        create_author()


def exit_program():
    console.print("Thanks for stopping in. Goodbye!", style="magenta")
    exit()


def read_(file):
    with open(file, "r") as file:
        return file.read()


if __name__ == "__main__":
    welcome()
