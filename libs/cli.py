from helpers import (
    exit_program,
    
)


def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        # if choice == "1":
            # author_first_name()
        else:
            print("Invalid choice")


def menu():
    print("Please select an option:")
    print("0. Exit the program")


if __name__ == "__main__":
    main()
