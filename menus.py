# Imports
from utilities import clear_terminal

# Start menu
def start_menu():
    print("What would you like to do?\n")
    print("1. Add new project\n2. View programming projects\n3. View everyday projects\n4. View archived projects\n5. Exit program\n\n")
    choice = str(input("Enter choice: "))
    if choice == "1":
        clear_terminal()
        add_project_menu()
    elif choice == "2":
        clear_terminal()
        view_programming()
    elif choice == "3":
        clear_terminal()
        view_everyday()
    elif choice == "4":
        clear_terminal()
        view_archive()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice, pick a number above")
        clear_terminal()
        start_menu()


# Project adding menu
def add_project_menu():
    print("Select project type:\n")
    print("1. Programming project\n2. Everyday project\n3. Return to main menu\n4. Exit program\n\n")
    choice = str(input("Enter choice: "))    
    if choice == "1":
        clear_terminal()
        ProgrammingProject.add_project_programming(programming_projects)# print(f"This is the returned list of programming projects:\n{programming_projects}")
    elif choice == "2":
        clear_terminal()
        EverydayProject.add_project_everyday(everyday_projects)# print(f"This is the returned list of everyday projects:\n{everyday_projects}")
    elif choice == "3":
        clear_terminal()
        start_menu()
    elif choice == "4":
        exit()
    else:
        print("Invalid choice, pick a number above")
        add_project_menu()


