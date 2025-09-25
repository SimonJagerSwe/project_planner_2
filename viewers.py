# Imports
import json
import menu_list

# from menu_list import add_project_menu, start_menu
from project_lists import ep_file, ea_file, fa_file, full_archive, pp_file, pa_file, programming_projects, programming_archive, everyday_projects, everyday_archive
from projects import modify_programming_project, modify_everyday_project, archive_project 
from utilities import clear_terminal

# View current programming projects
def view_programming():
    print("Viewing programming projects")
    try:
        with open(pp_file, "r") as file:
            projects = json.load(file)
            for i, project in enumerate(projects):
                print(f"{i + 1}. {project}\n")
    except:
        print("No programming projects available, returning to main menu...")
        menu_list.start_menu()

    choice = str(input("\n\nWhat do you want to do now?\n1. Add new project\n2. Modify project\n3. Archive project\n4. Return to main menu\n5. Exit program\n\nChoice: "))
    if choice == "1":
        clear_terminal()
        menu_list.add_project_menu()
    elif choice == "2":
        clear_terminal()
        modify_programming_project(pp_file, programming_projects)
    elif choice == "3":
        clear_terminal()
        archive_project(pp_file, programming_projects, pa_file, programming_archive, fa_file, full_archive)
    elif choice == "4":
        clear_terminal()
        menu_list.start_menu()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice")
        view_programming()


# View current everyday projects    
def view_everyday():
    print("Viewing everyday projects")
    try:
        with open(ep_file, "r") as file:
            projects = json.load(file)
            for i, project in enumerate(projects):
                print(f"{i + 1}. {project}\n")                
    except:
        print("No everyday projects available, returning to main menu...")
        menu_list.start_menu()        

    choice = str(input("\n\nWhat do you want to do now?\n1. Add new project\n2. Modify project\n3. Archive project\n4. Return to main menu\n5. Exit program\n\nChoice: "))
    if choice == "1":
        clear_terminal()
        menu_list.add_project_menu()
    elif choice == "2":
        clear_terminal()
        modify_everyday_project(ep_file, everyday_projects)
    elif choice == "3":
        clear_terminal()
        archive_project(ep_file, everyday_projects, ea_file, everyday_archive, fa_file, full_archive)
    elif choice == "4":
        clear_terminal()
        menu_list.start_menu()
    elif choice == "5":
        exit()
    else:
        print("Invalid choice")
        view_everyday()

# Programming archive viewer
def view_archive_programming():
    print("Viewing programming archive")
    with open(pa_file, "r") as file:
        try:
            archive = json.load(file)
            for i, project in enumerate(archive):
                print(f"{i + 1}. {project}")
        except:
            print("Currently no programming projects in archive")
            menu_list.view_archive()

    choice = str(input("\n\nWhat do you want to do now?\n1. Add new project\n2. Return to main menu\n3. Exit program\n\nChoice: "))
    if choice == "1":
        clear_terminal()
        menu_list.add_project_menu()
    elif choice == "2":
        clear_terminal()
        menu_list.start_menu()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")
        view_archive_programming()


# Everyday archive viewer
def view_archive_everyday():
    print("Viewing everyday project archive")
    try:
        with open(ea_file, "r") as file:
            archive = json.load(file)
            for i, project in enumerate(archive):
                print(f"{i + 1}. {project}")
    except:
        print("Currently no everyday projects in archive")
        menu_list.view_archive()

    choice = str(input("\n\nWhat do you want to do now?\n1. Add new project\n2. Return to main menu\n3. Exit program\n\nChoice: "))
    if choice == "1":
        clear_terminal()
        menu_list.add_project_menu()
    elif choice == "2":
        clear_terminal()
        menu_list.start_menu()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")
        view_archive_everyday()


# Full archive viewer
def view_full_archive():
    print("Viewing full archive")
    try:
        with open(fa_file, "r") as file:
            archive = json.load(file)
            for i, project in enumerate(archive):
                print(f"{i + 1}. {project}")
    except:
        print("Archive currently empty")
        menu_list.view_archive()
        
    choice = str(input("\n\nWhat do you want to do now?\n1. Add new project\n2. Return to main menu\n3. Exit program\n\nChoice: "))
    if choice == "1":
        clear_terminal()
        menu_list.add_project_menu()
    elif choice == "2":
        clear_terminal()
        menu_list.start_menu()
    elif choice == "3":
        exit()
    else:
        print("Invalid choice")
        view_full_archive()
