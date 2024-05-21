The AirBnB Clone Project

![AirBnB Logo](https://www.pngitem.com/pimgs/m/132-1322125_transparent-background-airbnb-logo-hd-png-download.png)

Welcome to the ALX Airbnb Console Project! This command-line interface (CLI) application is part of the ALX Full-Stack Software Engineer program. It represents the first step towards building a full web application: an AirBnB clone. This initial phase involves creating a custom command-line interface for data management and establishing the base classes for data storage.

Project Overview

This console, written in Python 3, facilitates CRUD operations (Create, Read, Update, Delete) on AirBnB objects such as User, City, Review, etc. This document provides an overview of the project's features, installation instructions, usage guidelines, and authors.

Features

User Authentication and Authorization: Securely manage user access. CRUD Operations: Create, read, update, and delete Airbnb listings. Advanced Search: Locate listings by location, price, availability, and other criteria. Booking Management: View and manage bookings and reservations. Reporting: Generate comprehensive reports and statistics on listings and bookings. Interactive Interface: Enjoy a user-friendly and interactive command-line experience.


Available commands:
- `show`
- `create`
- `update`
- `destroy`
- `count`

These commands allow users to create new objects, retrieve existing ones, perform operations on objects, update attributes, and delete objects.

Getting Started

Prerequisites
- Python 3.x

Installation

1. Clone the repository:
  sh
   git clone https://github.com/jzamora5/AirBnB_clone.git
  
2. Navigate to the project directory:
   sh
   cd AirBnB_clone
  

3. Run the console:
   sh
   ./console.py

File Structure

console.py	The main executable script for the command interpreter.

models/engine/file_storage.py	Handles the serialization and deserialization of instances to and from a JSON file.

models/__init__.py	Initializes the `FileStorage` instance.
models/base_model.py	Defines common attributes/methods for other classes.
models/user.py	User class inheriting from `BaseModel
models/state.py	State class inheriting from `BaseModel
models/city.py	City class inheriting from `BaseModel
models/amenity.py	Amenity class inheriting from `BaseModel
models/place.py	Place class inheriting from `BaseModel
models/review.py	Review class inheriting from `BaseModel

usage

The console can be operated in two modes: **Interactive** and **Non-interactive**.

Interactive Mode
In this mode, the console displays a prompt (`hbnb`) for user input.

Example:
sh
$ ./console.py
(hbnb) help

Documented commands (type help <topic>):
========================================
EOF  help  quit

(hbnb) quit
$


Non-interactive Mode
Commands are piped into the console's execution.

Example:
sh
$ echo "help" | ./console.py
(hbnb)

Documented commands (type help <topic>):
========================================
EOF  help  quit
(hbnb) 

Authors

@yonasghiwot

@dagm24
