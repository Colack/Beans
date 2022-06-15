# Generation Interpreter

import sys
import os
import time

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

getGenInput()
