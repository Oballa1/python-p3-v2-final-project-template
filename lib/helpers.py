from models.chefs import Chef
from models.meals import Meal
import sys

def exit_program():
    print("Exiting program.")
    sys.exit(0)

def add_chef():
    first_name = input("Enter the chef's first name: ")
    last_name = input("Enter the chef's last name: ")
    nick_name = input("Enter the chef's nickname: ")
    time_available = input("Enter the chef's available time: ")
    chef = Chef.create(first_name, last_name, nick_name, time_available)
    print(f"Added {chef}")

def list_chefs():
    chefs = Chef.get_all()
    if not chefs:
        print("No chefs found.")
    else:
        for chef in chefs:
            print(chef)

def find_chef_by_name():
    name = input("Enter the chef's name: ")
    chef = Chef.find_by_name(name)
    if chef:
        print(chef)
    else:
        print(f"No chef found with name {name}")

def add_meal():
    name = input("Enter the meal name: ")
    preparation_time = input("Enter the preparation time: ")
    days_prepared = input("Enter the days prepared: ")
    chef_id = input("Enter the chef ID: ")
    
    try:
        chef_id = int(chef_id)
        meal = Meal.create(name, preparation_time, days_prepared, chef_id)
        print(f"Added {meal}")
    except ValueError:
        print("Chef ID must be an integer.")

def list_meals():
    meals = Meal.get_all()
    if not meals:
        print("No meals found.")
    else:
        for meal in meals:
            print(meal)

def delete_chef():
    first_name = input("Enter the chef's first name: ")
    last_name = input("Enter the chef's last name: ")

    chef = Chef.find_by_name(first_name)
    if chef and chef.last_name == last_name:
        chef.delete()
        print(f"Deleted {chef}")
    else:
        print("Chef not found")

def delete_meal():
    name = input("Enter the meal name: ")

    meal = Meal.find_by_name(name)
    if meal:
        meal.delete()
        print(f"Deleted {meal}")
    else:
        print("Meal not found")
