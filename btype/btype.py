# BeansType Interpreter

import sys
import os
import time

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

getBtype()
