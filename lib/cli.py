from helpers import (
    exit_program,
    add_chef,
    list_chefs,
    add_meal,
    list_meals
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
            add_meal()
        elif choice == "4":
            list_meals()
        else:
            print("Invalid choice")

def menu():
    print("Please select an option:")
    print("0. Exit the program")
    print("1. Add a chef")
    print("2. List chefs")
    print("3. Add a meal")
    print("4. List meals")

if __name__ == "__main__":
    main()
