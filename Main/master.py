# Beans Master Interpreter
# Includes everything from Main, Generation, btype, DynamicSaur and DotBeans

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
version = "1.0"
manager = "Colack"
manager2 = "Colack"

def dynamic():
    print("== DynamicSaur ==")
    print("1. Libraries")
    print("2. Info")
    print("3. Exit")
    x = input("> ")
    if (x == 1):
        print("pun")
        print("A simple library for making if-statements and variables.")
        time.sleep(1)
        print("beans2")
        print("The original Beans! interpreter, with better keywords and easy to use tools.")
        time.sleep(1)
        print("skel")
        print("Generate 'skeleton' templates, with prefabs and simple ways to make your Beans! file yours.")
        time.sleep(1)
        dynamic()
    elif (x == 2):
        print("DynamicSaur is a offset/tool of Beans!")
        print("Coded by Colack")
        print("Managed by " + manager2)
        dynamic()
    else:
        sys.exit()

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

def getGenInput():
    fileName = input("Enter file name: ")
    try:
        file = open(fileName, "r")
        if (fileName.endswith(".bgen")):
            time.sleep(0.1)
        else:
            print("Invalid file type")
            time.sleep(1)
            getGenInput()
        if file.readline().startswith("Generation!"):
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print("Invalid file")
            getGenInput()
        
        for line in file:
            if line.startswith(":"):
                continue
            elif line.startswith("version"):
                print("Built for Beans version: " + line[8:], end="")
            elif line.startswith("build"):
                print("Build name: " + line[6:], end="")
            else:
                return "Invalid line"
            time.sleep(0.5)

    except FileNotFoundError:
        getGenInput()

def getBtype():
    fileName = input("Enter file name: ")
    try:
        file = open(fileName, "r")
        if (fileName.endsWith(".btype")):
            time.sleep(0.1)
        else:
            print("Invalid file type.")
            time.sleep(1)
            getBtype()
        if file.readline().startswith("Btype!"):
            os.system("cls" if os.name == "nt" else "clear")
        else:
            print("Invalid file.")
            getBtype()
        
        for line in file:
            if line.startswith("title"):
                print("Project: " + line[6:], end="")
            elif line.startswith("author"):
                print("Author: " + line[7:], end="")
            elif line.startswith("version"):
                print("Version: " + line[8:], end="")
            elif line.startswith("description"):
                print("Description: " + line[12:], end="")
            elif line.startswith("keywords"):
                print("Keywords: " + line[10:], end="")
            elif line.startswith("manager"):
                print("Manager: " + line[9:], end="")
            elif line.startswith("libs"):
                print("Libraries: " + line[5:], end="")
            elif line.startswith("main"):
                print("Main Beans file: " + line[5:], end="")
            elif line.startswith("end"):
                print("End of file.")
                break
            elif line.startswith(":"):
                continue
            else:
                print("Invalid line.")
                break
            time.sleep(0.5)

    except FileNotFoundError:
        print("Invalid file")
        getBtype()

def choices():
    x = input(":: ")
    if (x == ":help"):
        print(":main - Bootup main function.")
        time.sleep(0.1)
        print(":exit - Exits the program.")
        time.sleep(0.1)
        print(":gen - Opens up the Generation program.")
        time.sleep(0.1)
        print(":btype - Opens up the Btype program.")
        time.sleep(0.1)
        print(":dyna - Boots up the DynamicSaur libraries program.")
        time.sleep(0.1)
        print(":dotbeans - Boots up the DotBeans program.")
        time.sleep(0.1)
        print(":credits - Displays the credits of the program.")
    elif (x == ":main"):
        main()
    elif (x == ":exit"):
        sys.exit()
    elif (x == ":gen"):
        getGenInput()
    elif (x == ":btype"):
        getBtype()
    elif (x == ":dyna"):
        dynamic()
    elif (x == ":dotbeans"):
        dotbeans()
    elif (x == ":credits"):
        cred()
    else:
        print("Invalid command")
        print("Use ':help' for help")
        choices()

def dotbeans():
    x = input("Enter file destination (. for current dir.): ")
    if (x == "."):
        z = ".beans"
        os.mkdir(".beans")
    else:
        z = x + ".beans"
        os.mkdir(x + ".beans")
    print("Creating a .bgen file...")
    y = input("Project name: ")
    file = open(z + "/" + y + ".bgen", "w")
    file.write("Generation!\n")
    a = input("Current Version: ")
    file.write("version " + a + "\n")
    b = input("Build: ")
    file.write("build " + b + "\n")
    file.close()
    print(".bgen file created.")
    print("Now creating a .btype file.")
    file = open(z + "/" + y + ".btype", "w")
    file.write("Btype!\n")
    file.write("title " + y + "\n")
    c = input("Author: ")
    file.write("author " + c + "\n")
    d = input("Manager: ")
    file.write("manager " + d + "\n")
    e = input("Description: ")
    file.write("description " + e + "\n")
    file.write("version " + a + "\n")
    f = input("Keywords: ")
    file.write("keywords " + f + "\n")
    g = input("Libraries: ")
    file.write("libs " + g + "\n")
    h = input("Main file: ")
    file.write("main " + h + "\n")
    file.write("end\n")
    file.close()
    print(".btype file created.")
    print("Finished!")
  
def cred():
    print("Credits: ")
    print("Concept by Colack")
    print("\n")
    print("Contributors: ")
    print("Colack")
    print("Managed by " + manager + ".")
    x = input("Press anything to continue.")

choices()
