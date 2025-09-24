# Imports
import os
import sys

from menus import start_menu


# Clear terminal
def clear_terminal():
    os.system("cls" if os.name == "nt" else "clear")


# Exit program
def exit():
    choice = input("Are you sure you want to quit? Y/N: ").lower()
    if choice == "y":
        sys.exit("\nExiting program")
    elif choice == "n":
        start_menu()
    else:
        print("Invalid option, type 'Y' for yes or 'N' for no")
        exit()