##Overview
This project is a CLI-based system to manage chefs and meals within a culinary context. The system allows users to add, list, find, and delete chefs and meals. It also demonstrates interaction with a SQLite database to persist data. Below is a detailed description of the important files, functions, and models in the project.

Functions
main(): This is the entry point of the script. It runs an infinite loop, presenting a menu to the user and executing the corresponding functions based on the user's input.
menu(): Prints the available options to the user.
Helper Functions: helpers.py
This file contains functions that perform the core actions of the CLI script, such as adding, listing, finding, and deleting chefs and meals. Each function interacts with the models to perform database operations.

Functions
exit_program(): Exits the program.
add_chef(): Prompts the user to enter details of a new chef and saves it to the database.
list_chefs(): Retrieves and prints all chefs from the database.
find_chef_by_name(): Prompts the user to enter a chef's name and retrieves the chef from the database if found.
add_meal(): Prompts the user to enter details of a new meal and saves it to the database.
list_meals(): Retrieves and prints all meals from the database.
delete_chef(): Prompts the user to enter the first name and last name of a chef to be deleted and removes the chef from the database if found.
delete_meal(): Prompts the user to enter the name of a meal to be deleted and removes the meal from the database if found.

models/chef.py
Chef Class
__init__(self, first_name, last_name, nick_name, time_available, chef_id=None): Initializes a new chef instance.
__repr__(self): Returns a string representation of the chef.
create_table(cls): Creates the chefs table in the database if it doesn't exist.
drop_table(cls): Drops the chefs table from the database.
save(self): Inserts a new chef record into the database.
create(cls, first_name, last_name, nick_name, time_available): Creates and saves a new chef instance.
update(self): Updates the chef record in the database.
delete(self): Deletes the chef record from the database.
instance_from_db(cls, row): Creates a chef instance from a database row.
get_all(cls): Retrieves all chefs from the database.
find_by_name(cls, name): Finds a chef by their first or last name.
find_by_id(cls, chef_id): Finds a chef by their ID.
dishes(self): Retrieves all dishes associated with the chef.
