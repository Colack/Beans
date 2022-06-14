import sys
import os
import time

def main():
    x = input("Enter file destination (. for current dir.): ")
    if (x == "."):
        z = ".beans"
        os.mkdir(".beansproject")
    else:
        z = x + ".beansproject"
        os.mkdir(x + ".beansproject")
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

main()
