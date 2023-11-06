from helpers import (
    exit_program, list_madlibs, list_categorys
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            list_madlibs()
        elif choice == "2":
            list_categorys()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. List MadLibs")
    print("2. List categories")


if __name__ == "__main__":
    main()
