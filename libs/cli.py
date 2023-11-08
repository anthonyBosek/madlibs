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
    console.print(read_("./libs/txts/welcome.txt"), style="magenta")
    choice = input("").lower()
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
         
     


# def create_author():
#     global current_author
#     subprocess.call("clear")
#     console.print("Enter your first name: ", style="cyan underline bold")
#     first_name = input("> ").strip()
#     console.print("Enter your last name: ", style="cyan underline bold")
#     last_name = input("> ").strip()
#     subprocess.call("clear")
#     console.print(f"Hello {first_name} {last_name}", style="cyan underline bold")
#     print()
#     current_author = author.Author.create(first_name, last_name)
#     select_category()

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



# def select_category():
#     console.print(read_("./libs/txts/categories.txt"), style="yellow")
#     all_cats = template.Template.get_all_categorys()
#     i = 1
#     for cat in all_cats:
#         print(f"{i}. {cat}")
#         i += 1
#     category = input("> ").strip()
#     while not category:
#         console.print("Please select a category by number!")
#         category = input("> ").strip()
#     cat = all_cats[int(category) - 1]
#     enter_words(cat)
    
    # enter_words(template.Template.random_template(all_cats[int(category) - 1]))
    
def select_category():
    while True:
        console.print(read_("./libs/txts/categories.txt"), style="yellow")
        all_cats = template.Template.get_all_categorys()
        i = 1
        for cat in all_cats:
            print(f"{i}. {cat}")
            i += 1
        
        category = input("> ").strip()
        
        try:
            category_index = int(category)
            if 1 <= category_index <= len(all_cats):
                cat = all_cats[category_index - 1]
                enter_words(cat)
                break  # Exit the loop when a valid category is selected
            else:
                subprocess.call("clear")
                console.print("Invalid category number. Please select a valid category by number.")
        except ValueError:
            subprocess.call("clear")
            console.print("Please select a category by entering its number.")
        except IndexError:
            subprocess.call("clear")
            console.print("Invalid category number. Please select a valid category by number.")

# # Call the select_category function to choose a category
# select_category()









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
    # print(madlib)
    # print(current_template)

    # new_madlib = current_template[4] 
    new_madlib = current_template[3]
    # regex=r"\[\d{,2}\]"
    author_words = madlib.author_words_list.split(",")
    story = re.sub(r"\[\d{,2}\]", lambda x:author_words[int(x.group()[1])], new_madlib)
    print("Here's your new MadLib!")
    print(current_template[2])
    print(story)

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


