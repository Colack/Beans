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
        print("README")
        print("Beans is not Markdown!")
        print("Create Markdown files easily with Beans, with easy keywords to memorize.")
        print("The creation of Markdown files will never be hard again!")
        print("\n")
        print("Example: (Beans code)")
        print("\n")
        print("beans init (Start the beans program)")
        print("beans create (Create a new file)")
        print("header I love beans (Create a header with the text I love beans)")
        print("print Beans are so cool (Add a line of text underneath the header)")
        print("console I love beans! (Log a line of text to the console)")
        print("\n")
        print("The output of the above code will look like this:")
        print("\n")
        print("I love beans")
        print("Beans are so cool")
        print("\n")
        main()

    elif user_input == "2":
        print("")

    elif user_input == "3":
        sys.exit()

def clear():
    print("\n" * 100)

main()
