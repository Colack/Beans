import sys
import os
import time 

manager2 = "Colack"

def main():
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
        main()
    elif (x == 2):
        print("DynamicSaur is a offset/tool of Beans!")
        print("Coded by Colack")
        print("Managed by " + manager2)
        main()
    else:
        sys.exit()
        
main()
