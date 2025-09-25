# Imports
from project_lists import programming_projects, everyday_projects
from projects import ProgrammingProject, EverydayProject
from utilities import clear_terminal
from viewers import view_programming, view_everyday, view_archive_programming, view_archive_everyday, view_full_archive

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

# Archive viewer menu
def view_archive():
    print("Select which archive to view:\n")
    print("1. Programming projects archive\n2. Everyday projects archive\n3. Full achive\n4. Return to main menu\n5. Exit program\n\n")
    choice = str(input("Enter choice: "))
    if choice == "1":
        clear_terminal()
        view_archive_programming()
    elif choice == "2":
        clear_terminal()
        view_archive_everyday()
    elif choice == "3":
        clear_terminal()
        view_full_archive()
    elif choice == "4":
        clear_terminal()
        start_menu()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice, pick a number above")
        view_archive()
