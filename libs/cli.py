from helpers import (
    exit_program,
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        else:
            print("Invalid choice")
def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. create a new author")

if __name__ == "__main__":
    main()
