# AAA MadLibs

AAA MadLibs is a python command line application were the user and add their info to the data base, and pick through a list of categories that will provided a random madlib template that the user can then fill out the words list to complete the madlib. After completion the application will display the completed madlib and give the user the option to save or delete the madlib. After completing multiple madlibs the user can view and delete their saved madlibs. Finaly the user can delete their information from the data base. 

## Intro To Project

- This project was made to complete the `Phase 3 Project` python assignment for the `SE-West-091123` class for the [Flatiron](https://flatironschool.com/) Software Engineering Boot Camp.
- The project was completed using the following: `Python3`, `SQLite`, `asciart`, `rich`.

## Installation

* fork and clone this repository to your local machine
* install pipenv <br>
 ```pipenv install```
 * initiate pipenv shell <br> ```pipenv shell```
* install rich <br> ```pip install rich```
* access the Command Line Interface <br> ```python libs/cli.py```

## Using the Application

- The user will be prompted on the welcome page to "start" the application, "exit" the application, or inquire for "help" (which will bring up an info menu and list of commands) by entering one of the three "-start", "-exit", "-help". If any other input is entered the user will receive an error message. 
- After starting the application the user will be required to enter ther information (first and last name) which will be stored into theauthor data table to track each users madlibs.
- Once the user has entered ther information they will be propmpted to choose a category of madlibs by its corrisponding number from our list of categories to generate a random madlib template from that category.
- The random template will prompt the user with a list of words to fill out that will be inputed into the templates text.
- After the user fills out the list of words the application will print out the finished madlib with the users words and give the user the option to either save or delete the created madlib.
- The user can then view their saved madlibs and have the ablitiy to delete them.
- The user has the ability to remove their information from the data base.


## License

- This project is is made in conjunction with the standard `MIT` license provided by `GitHub` upon creation of a new repository. A copy of the license is included with this project in a file named: `LICENSE`.


## What I Learned

- `Anthony`:
- `Austin`: I learned alot working on this project. This was my first python project and first command line application. It was a different experience not being able to see things and debug in the console, but it taught me houw to use pytyons debugger and how to debug code in a new way. Also, working with the sqlite data base was new and diffrent from the json data bases that I have work with prior. This project and my grouo mates Anthony nad Alberto have taught me alot about python and backend development.
- `Alberto`:

* [Back To Top](#AAA-MadLibs)
