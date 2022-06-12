# Beans interpreter

import sys
import os
import time

libs = [
    "pun",
    "beans2",
    "skel"
]
keywords = [
    ":",
    "header",
    "print",
    "wait",
    "can"
]
timeStarted = False
fileType = ""

def getFileInput():
    fileName = input("Enter file name: ")
    try:
        file = open(fileName, "r")
        if file.readline().startswith("Beans!"):
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print("Invalid file")
            getFileInput()

        for line in file:
            timeStarted = False
            if line.startswith(":"):
                continue
            elif line.startswith("header"):
                print(line[7:], end="")
                print("-----");
            elif line.startswith("print"):
                print(line[6:], end="")
            elif line.startswith("wait"):
                time.sleep(float(line.split(" ")[1]))
                timeStarted = True
            elif line.startswith("can"):
                if line.split(" ")[1] in libs:
                    continue
                else:
                    return "Invalid library"
            else:
                return "Invalid line"
            if timeStarted == False:
                time.sleep(0.5)
            else:
                continue

        file.close()
        time.sleep(5)
        x = input("Press enter to continue...")

    except FileNotFoundError:
        print("File not found")
        return getFileInput()

def main():
    print("Beans V1.0")
    print("Type ':help' for help")
    x = input("> ")
    if (x == ":help"):
        print("x")
    elif (x == ":exit"):
        sys.exit()
    elif (x == ":clear"):
        os.system("cls" if os.name == "nt" else "clear")
    elif (x == ":run"):
        getFileInput()
    elif (x == ":libs"):
        print("Included libraries:")
        for lib in libs:
            print(lib)
        for file in os.listdir('.'):
            if file.startswith("!"):
                print(file[1:])
            else:
                continue
    elif (x == ":beans"):
        choiceStuff()
    else:
        print("Invalid command")
        main()

def choiceStuff():
     while True:
        os.system("cls" if os.name == "nt" else "clear")
        print("1. Interpreter")
        print("2. Compiler")
        print("3. Exit")
        choice = input("> ")
        if choice == "1":
            getFileInput()
        elif choice == "2":
            print("Compiler")
        elif choice == "3":
            sys.exit()
        else:
            print("Invalid choice")
            print("Use ':help' for help")
            time.sleep(1)
            main()

def compiler():
    file = input("Enter file name: ")
    file.open(file, "r")
    if file.readline().startswith("Beans!"):
        print("File cannot be a beans file.")
        print("Try Beans, Markdown, or a text file.")
    elif file.readline().startswith("Md!") or file.readline().startswith("MD!") or file.readline().startswith("md!"):
        fileType = "md"
    elif file.readline().startswith("Txt!") or file.readline().startswith("txt!") or file.readline().startswith("TXT!"):
        fileType = "txt"
    else:
        print("Invalid file type.")
        print("Try Beans, Markdown, or a text file.")
        main()

    # Make a new file with the same name as the original
    f = open(file + "." + fileType, "w")
    
    


        


main()
