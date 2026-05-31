# SIMPLE TASK MANAGER (PYTHON)

A simple command-line task manager written in Python. This application allows users to create, view, add, and delete tasks stored in a local text file.

## FEATURES

* Create a task file automatically if it does not exist.
* Add new tasks to a text file.
* Display all saved tasks.
* Delete all tasks from the file.
* Cross-platform console clearing (Windows, Linux, and macOS).
* Simple menu-driven interface.

## REQUIREMENTS

* Python 3.x

No external libraries are required.

## INSTALLATION

1. Clone or download the project files.
2. Make sure the Python script is in the same directory where you want the task file to be stored.
3. Run the script:

python main.py

## USAGE

When the program starts, you will see the following menu:

What do you want to do?

1. Add tasks
2. Clear tasks
3. Show tasks
4. Exit

## ADD TASKS

Select option 1 to add new tasks.

* Type a task and press Enter.
* The task will be appended to tareas.txt.
* Type "salir" to return to the main menu.

## CLEAR TASKS

Select option 2 to access the delete menu.

Options:

1. Clear all tasks
2. Exit

Choosing option 1 will permanently remove all saved tasks.

## SHOW TASKS

Select option 3 to display all stored tasks.

To return to the main menu, enter:

1

## EXIT

Select option 4 to close the application.

## FILE STRUCTURE

project/

|-- main.py
|-- tareas.txt

* main.py    : Main application script.
* tareas.txt : Stores all tasks entered by the user.

## HOW IT WORKS

The program automatically creates a file named "tareas.txt" if it does not already exist. Tasks are stored line by line in this file. The application reads, writes, and clears the file depending on the user's menu selection.

## POSSIBLE IMPROVEMENTS

* Delete individual tasks.
* Mark tasks as completed.
* Add task categories.
* Store tasks using JSON or a database.
* Improve input validation.
* Add timestamps for tasks.
* Support task priorities.

## LICENSE

This project is open-source and can be freely modified and distributed for educational purposes.
