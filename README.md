# Phase 3 -WK3 - Code Challenge: Articles - with database
## Magazine & Article Management System.
Welcome to the Magazine Article Management System! This project is designed to manage the relationships between authors, articles, and magazines. It allows you to create authors, assign articles to them, and link articles to magazines. The system enables exploring various features such as searching for authors by their articles, finding contributors to specific magazines, and more.

## Set Instructions

To get started, while inside of this directory.
  - run `pipenv install` 
  - run `pipenv shell` to jump into the shell. 
  - run `python3 app.py` to create the database

## Overview
The system is built using Python and SQLite, allowing for the management of three main entities:

Author
Magazine
Article

An Author can have many Articles, and a Magazine can contain many Articles. The relationship between Author and Magazine is many-to-many, where articles link both authors and magazines.

## Core Deliverables

Write the following methods in the models(Article, Author, magazine) provided in the models folder. Feel free to build out any helper methods if needed.

### Initializers and Properties

#### Author

- `Author __init__(self, id, name)`
  - Author is initialized with a name
  - This initialization should create a new entry in the database `authors` table
- `Author property id`
  - Returns the id of the newly created `Author`
  - Names must be of type `int`
  - Remember to use the setter and getter method for easy retrieval, since this will be needed when creating `articles`
- `Author property name`
  - Returns the author's name
  - The value of the name property should derive from the database `authors`. You should makes use of getters and setters methods to manipulate this property.
  - Names must be of type `str`
  - Names must be longer than 0 characters
  - Should **not be able** to change after the author is instantiated.
  - _hint: hasattr()_

#### Magazine

- `Magazine __init__(self, id, name, category)`
  - A magazine is initialized with a name and a category
  - This initialization should create a new entry in the database `magazines` table 
- `Author property id`
  - Returns the id of the newly created `Magazine`
  - id must be of type `int`
  - Remember to use the setter and getter method for easy retrieval, since this will be needed when creating `articles`
- `Magazine property name`
  - Returns the magazine's name
  - The value of the name property should derive from the database `magazines`. You should makes use of getters and setters methods to manipulate this property.
  - Names must be of type `str`
  - Names must be between 2 and 16 characters, inclusive
  - Should **be able** to change after the magazine is instantiated.
- `Magazine property category`
  - Returns the magazine's category
  - The value of the category property should derive from the database `magazines`. You should makes use of getters and setters methods to manipulate this property.
  - Categories must be of type `str`
  - Categories must be longer than 0 characters
  - Should **be able** to change after the magazine is instantiated.

#### Article

- `Article __init__(self, author, magazine, title)`
  - Article is initialized with an `Author` instance, a `Magazine` instance, and a title. 

  NB: Creating a new entry in the `article` table requires the author and magazine PKs(Primary Keys) as FKs(Foreign Keys). Find a way to retrive the author and maagzine id properties from their respective models then use them here
  - The initialization should create a new entry in the database `articles` table
- `Article property title`
  - Returns the article's title
  - Titles must be of type `str`
  - Titles must be between 5 and 50 characters, inclusive
  - Should **not be able** to change after the article is instantiated.
  - _hint: hasattr()_

### Object Relationship Methods and Properties

#### Article

- `Article property author`
  - Write a method in the Article model that returns the author of the article.
  - You can make use of the SQL JOINS to achieve this

- `Article property magazine`:
   - Write a method in the Article model that returns the magazine of the article.
  - You can make use of the SQL JOINS to achieve this

#### Author

- `Author articles()`
  - Write a method called articles() in the Author model that will return all articles associated with an author
  - Remember to make use of the SQL JOINS concept to achieve this
- `Author magazines()`
  - Write a method called magazines() in the Author model that will return all magazines associated with an author
  - Remember to make use of the SQL JOINS concept to achieve this

#### Magazine

- `Magazine articles()`
  - Write a method called articles() in the Magazine model that will return all articles associated with a Magazine
  - Remember to make use of the SQL JOINS concept to achieve this

- `Magazine contributors()`
  - Write a method called contributors() in the Magazine model that will return all Authors associated with a magazine
  - Remember to make use of the SQL JOINS concept to achieve this

### Aggregate and Association Methods

#### Magazine

- `Magazine article_titles()`
  - Write a article_titles() method in the magazine model that returns a list of the titles strings of all articles written for that magazine
  - Returns `None` if the magazine has no articles
- `Magazine contributing_authors()`
  - Write a contributing_authors() in the Magazine model that returns a list of authors who have written more than 2 articles for the magazine
  - Authors must be of type `Author`
  - Returns `None` if the magazine has no authors with more than 2 publications

## Setup
Requirements:
Python 3.x
SQLite3 (Database)

## Steps to Run:
Clone the repository to your local machine.
Install the required dependencies:
pip install sqlite3
Run the system in a Python environment.

## Running the Program:
Open a terminal in the project directory.
To test the application, simply run pytest to ensure all tests pass.

## Development
To contribute or develop additional features, follow these steps:

Fork the repository.
Create a new branch for your feature:
git checkout -b feature-name
Commit your changes:
git commit -m "Your commit message"
Push the changes to your branch:
git push origin feature-name
Open a pull request with a description of the changes made.

## Technologies Used
Python 3.x: The programming language used to build the system.
SQLite: The database used to store authors, articles, and magazines.
Object-Oriented Programming: Employed to model the relationships between authors, articles, and magazines.

## Acknowledgments
Python: A versatile programming language used to build the system.
Object-Oriented Programming: Implemented to efficiently manage the relationships between authors, articles, and magazines.
SQLite: Used for database management and storage of the application data.



