from helpers import (
    exit_program,
    add_chef,
    list_chefs,
    find_chef_by_name,
    add_meal,
    list_meals,
    delete_chef,
    delete_meal
)

def main():
    while True:
        menu()
        choice = input("> ")
        if choice == "0":
            exit_program()
        elif choice == "1":
            add_chef()
        elif choice == "2":
            list_chefs()
        elif choice == "3":
            find_chef_by_name()
        elif choice == "4":
            add_meal()
        elif choice == "5":
            list_meals()
        elif choice == "6":
            delete_chef()
        elif choice == "7":
            delete_meal()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a chef")
    print("2. List chefs")
    print("3. Find chef by name")
    print("4. Add a meal")
    print("5. List meals")
    print("6. Delete a chef")
    print("7. Delete a meal")

if __name__ == "__main__":
    main()
