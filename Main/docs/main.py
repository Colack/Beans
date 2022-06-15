import sys
import docsStuff

hasShown = False
hasShown2 = False

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
        print("beans init (Start a beans program)")
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
        print("Documentation")
        if (hasShown2 == False):
            print("Beans is a alternative to Markdown.")
            print("It has many uses.")
            print("It is essentially a Markdown/Text file, with extra features and tools you can use.")
            print("Example: (Beans Code)")
            print("\n")
            print("beans init (Start a beans program)")
            print("beans create (Create a new file.")
            print("header I love beans (Create a header with the text I love beans)")
            print("print Beans are so cool (Add a line of text underneath the header)")
            print("console I love beans! (Log a line of text to the console)")
            hasShown2 = True

        else:
            print("Welcome to the Beans Documentation!")
        
        print("\n")
        print("\n")
        print("\n")
        print("1. A Introduction to Beans")
        print("2. A Quick Start Guide")
        print("3. A Quick Start Guide (2)")
        print("4. Different uses with Beans")
        print("5. Compiling Beans to .md and .txt")
        print("6. Further Documentation")
        print("7. Extra Features and Notes")
        print("8 Final Notes")
        print("9. Acknowledgements")
        print("10. License")
        print("11. Credits")
        print("12. Exit")
        print("\n")

        user_input2 = input("Please enter a number: ")

        if user_input2 == "1":
            docsStuff.intro()
        
        elif user_input2 == "2":
            print("\n")

        elif user_input2 == "3":
            print("\n")

        elif user_input2 == "4":
            print("\n")

        elif user_input2 == "5":
            print("\n")

        elif user_input2 == "6":
            print("\n")

        elif user_input2 == "7":
            print("\n")

        elif user_input2 == "8":
            print("\n")

        elif user_input2 == "9":
            print("\n")

        elif user_input2 == "10":
            print("\n")

        elif user_input2 == "11":
            print("\n")

        elif user_input2 == "12":
            sys.exit()

    elif user_input == "3":
        sys.exit()

def clear():
    print("\n" * 100)

main()
