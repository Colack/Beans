import sys

hasShown = False

def main(): 
    if hasShown == False:
        print("Welcome to Beans!")
        print("This file is a README/Documentation file for the Beans project.")
        clear()
        hasShown = True
    else:
        clear()

    print("Menu: ")
    print("1. Readme")
    print("2. Documentation")
    print("3. Exit")
    user_input = input("Please enter a number: ")

    if user_input == "1":
        print("")

    elif user_input == "2":
        print("")

    elif user_input == "3":
        sys.exit()

def clear():
    print("\n" * 100)

main()
