# Beans Interpreter

import sys
import os
import time

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

getFileInput()
