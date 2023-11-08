# AAA MadLibs
AAA MadLibs is a python command line application were the user and add their info to the data base, and pick through a list of categories that will provided a random madlib template that the user can then fill out the words list to complete the madlib. After completion the application will display the completed madlib and give the user the option to save or delete the madlib. After completing multiple madlibs the user can view and delete their saved madlibs. Finaly the user can delete their information from the data base. 

## Intro To Project

- This project was made to complete the `Phase 3 Project` python assignment for the `SE-West-091123` class for the [Flatiron](https://flatironschool.com/) Software Engineering Boot Camp.
- The project was completed using the following: `Python3` and `rich`.

## Installation
---
* fork and clone this repository to your local machine
* install pipenv <br>
 ```pipenv install```
* install simple-chalk <br> ```pip install simple_chalk```
* initiate pipenv shell <br> ```pipenv shell```
* navigate to the **lib** directory on your local terminal <br>
 ```cd lib```
* access the Command Line Interface <br> ```python3 cli.py```

## Application Features

* [Dependencies](#dependencies)
* [Starting the Application](#starting-the-application)
* [Using the Application](#using-the-application)
* [Optional Features](#optional-features)
* [License](#license)
* [Attributions](#attributions)
* [What I Learned](#what-i-learned)





<!-- ## Dependencies

- The following is needed to run this application: `Python`, `rich`.

- You must have access to these dependencies in the directory that you are running this application in. If your environment does not have these requirements, you may install them in this order by going to these websites and following the installation instructions:

- [Npm - Node.JS](https://www.npmjs.com/package/node)

- [Npm - JSON Server](https://www.npmjs.com/package/json-server) -->


<!-- ## Starting the Application

- Make sure nothing is currently running on `http://localhost:3000`.
- Open a terminal window in the main directory of where this project is located on your computer.
- Run `json-server --watch db.json`.
- It should be running on `http://localhost:3000` and your terminal should look something like this:
- ==============================================
    ![JSON Server running correctly.](./assets/server-pic.png "JSON Server")
- ==============================================
- Open another terminal window in the main directory of where this project is located on your computer
- Run `open index.html`.
- It should take you to a page that looks like this:
- ==============================================
    ![Home page of app.](./assets/index.png "Home Page")
- ============================================== -->


## Using the Application

- The user will be prompted on the welcome page to "start" the application, "exit" the application, or inquire for "help" (which will bring up an info menu and list of commands) by entering one of the three "-start", "-exit", "-help". If any other input is entered the user will receive an error message. 
- After starting the application the user will be required to enter ther information (first and last name) which will be stored into theauthor data table to track each users madlibs.
- Once the user has entered ther information they will be propmpted to choose a category of madlibs by its corrisponding number from our list of categories to generate a random madlib template from that category.
- The random template will prompt the user with a list of words to fill out that will be inputed into the templates text.
- After the user fills out the list of words the application will print out the finished madlib with the users words and give the user the option to either save or delete the created madlib.
- The user can then view their saved madlibs and have the ablitiy to delete them.
- The user has the ability to remove their information from the data base.


## Optional Features

- The user can adjust the order in which the cards are listed by selecting the different options located at the top of every column. For example, the user can click on the 'Name' option and sort the list alphabetically or the reverse.
- The user can switch the color theme of the app by clicking the moon located in the top right area of the page, to the right of the search bar.
- It should look like this:
- ==============================================
    ![Home page of app.](./assets/dark-index.png "Home Page")
- ==============================================


## License

- This project is is made in conjunction with the standard `MIT` license provided by `GitHub` upon creation of a new repository. A copy of the license is included with this project in a file named: `LICENSE`.


## Attributions

- The project was completed with collaboration from: `Anthony Bosek`, `Austin Ohlfs`, and `Alberto Sierra`
- This project was created with combination of skills learned from the `Flatiron` curriculum and our own individual research.
- The data used to seed the original data prior to being modified for the purposes of this project was supplied by [Pokedex](https://rapidapi.com/lduran2-CvRRB1hLBCj/api/pokedex2) created by `Luis Duran`.
- And of course, [Stack Overflow](https://stackoverflow.com/).

## What I Learned

- `Anthony`:
- `Austin`: 
- `Alberto`:

* [Back To Top](#table-2-phase-1-project)
