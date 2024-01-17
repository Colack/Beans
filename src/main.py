# Beans interpreter

import sys
import os
import time

# Libraries will be added in a later update
libs = [
    ""
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
version = "1.0"
manager = "Colack"

def getFileInput():
    fileName = input("Enter file name: ")
    try:
        file = open(fileName, "r")
        if (fileName.endswith(".beans")):
            time.sleep(0.1)
        else:
            print("Invalid file type")
            time.sleep(1)
            getFileInput()
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
            elif line.startswith("clear"):
                os.system("cls" if os.name == "nt" else "clear")
            elif line.startswith("table"):
                x = line[6:]
                if x.startswith("start"):
                    print("|=|")
                elif x.startswith("end"):
                    print("|=|")  
                elif x.startswith("line"):
                    print("---")
            elif line.startswith("line"):
                print("-----")
            elif line.startswith("bold"):
                print("\033[1m" + line[7:] + "\033[0m", end="")
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
        getFileInput()

def main():
    print("Beans V" + version)
    print("Type ':help' for help")
    x = input("> ")
    if (x == ":help"):
        print("Beans is a simple system for creating readme files.")
        time.sleep(0.1)
        print("It is a simple language with a very small syntax.")
        time.sleep(0.1)
        print("Shell Commands: ")
        time.sleep(0.1)
        print(":help - Displays this help message")
        time.sleep(0.1)
        print(":exit - Exits the program")
        time.sleep(0.1)
        print(":run - Runs a file")
        time.sleep(0.1)
        print(":clear - Clears the screen")
        time.sleep(0.1)
        print(":version - Displays the version of the program")
        time.sleep(0.1)
        print(":license - Displays the license of the program")
        time.sleep(0.1)
        print(":credits - Displays the credits of the program")
        time.sleep(0.1)
        print(":libs - Displays all libraries to use")
        time.sleep(0.1)
        print(":build - Displays the build of the program")
        main()
    elif (x == ":exit"):
        sys.exit()
    elif (x == ":clear"):
        os.system("cls" if os.name == "nt" else "clear")
        time.sleep(0.1)
        main()
    elif (x == ":run"):
        getFileInput()
    elif (x == ":libs"):
        print("Included libraries:")
        for lib in libs:
            print(lib)
        main()
    elif (x == ":version"):
        print("Beans V" + version)
        time.sleep(1)
        main()
    elif (x == ":license"):
        print("Beans is licensed under the MIT license.")
        time.sleep(1)
        main()
    elif (x == ":credits"):
        print("Beans was created by Colack.")
        print("It is currently managed by " + manager)
        time.sleep(1)
        main()
    elif (x == ":build"):
        print("Beans Zen Build")
        time.sleep(1)
    else:
        print("Invalid command")
        print("Use ':help' for help")
        time.sleep(1)
        main()

main()
