# Imports
import json


from datetime import datetime
from menus import start_menu
from project_lists import pp_file, ep_file

# Project class, initializing project parameters 
class Project:
    def __init__(self, name, start, finish, progress, status):
        self.name = name
        self.start = start
        self.finish = finish
        self.progress = progress
        self.status = status
        

# Programming class, project parameters from parent class, and additional
class ProgrammingProject(Project):
    def __init__(self, name, start, finish, progress, status, language, link):
        super().__init__(name, start, finish, progress, status, language, link)
        self.language = language
        self.link = link
    

    # Add programming project function
    def add_project_programming(pp):
        name = input("Project name: ")
        start = input("Project start date (if today, leave empty and press enter): ")
        if start == "":
            start = datetime.today().strftime("%Y-%m-%d")
        finish = input("Projected finish date (if today, leave empty and press enter): ")
        if finish == "":
            finish = datetime.today().strftime("%Y-%m-%d")
        language = input("Project language(s): ")
        link = input("Project link: ")
        progress = input("Project progress: ")
        status = input("Project status: ")
        project = {
            "name" : name,
            "start" : start,
            "finish" : finish,
            "language" : language,
            "link" : link,
            "progress" : progress,
            "status" : status
            }
        pp.append(project)

        with open(pp_file, "w") as file:
            json.dump(pp, file)
        
        start_menu()


# Everyday class, utilizing parameters from parent class
class EverydayProject(Project):
    def __init__(self, name, start, finish, progress, status):
        super().__init__(name, start, finish, progress, status)


    # Add everyday project function
    def add_project_everyday(ep):
        name = input("Project name: ")
        start = input("Project start date (if today, leave empty and press enter): ")
        if start == "":
            start = datetime.today().strftime("%Y-%m-%d")
        finish = input("Project finish date (if today, leave empty and press enter): ")
        if finish == "":
            finish = datetime.today().strftime("%Y-%m-%d")
        progress = input("Project progress: ")
        status = input("Project status: ")
        project = {
            "name" : name,
            "start" : start,
            "finish" : finish,
            "progress" : progress,
            "status" : status
            }        
        ep.append(project)

        with open(ep_file, "w") as file:
            json.dump(ep, file)

        start_menu()


# Modifying programming projects, calling programming projects file and list
def modify_programming_project(pf, pl):
    pl.clear()
    with open(pf, "r") as file:
        projects = json.load(file)
        for i, project in enumerate(projects):
            print(f"{i + 1}. {project}\n")
            pl.append(project)
    
        choice = int(input("Chose project number to modify: "))
        project_to_change = projects[choice - 1]
        # print(project_to_change)
        print("If project variable is to be unchanged, just press Enter")           
        name = input("Project name: ")
        if name == "":
            name = project_to_change["name"]
        start = input("Project start date: ")
        if start == "":
            start = project_to_change["start"]
        finish = input("Projected finish date: ")
        if finish == "":
            finish = project_to_change["finish"]
        language = input("Project language(s): ")
        if language == "":
            language = project_to_change["language"]
        link = input("Project link: ")
        if link == "":
            link = project_to_change["link"]
        progress = input("Project progress: ")
        if progress == "":
            progress = project_to_change["progress"]
        status = input("Project status: ")
        if status == "":
            status = project_to_change["status"]
        changed_project = {
            "name" : name,
            "start" : start,
            "finish" : finish,
            "language" : language,
            "link" : link,
            "progress" : progress,
            "status" : status
            }
        print(f"Project to change: {project_to_change}")
        print(f"Project changed to: {changed_project}")
        pl.remove(project_to_change)
        pl.append(changed_project)
        print(pl)

        with open(pp_file, "w") as file:
            json.dump(pl, file)

    start_menu()


# Modify everyday project, calling the everyday projects file and list
def modify_everyday_project(ef, el):
    el.clear()
    with open(ef, "r") as file:
        projects = json.load(file)
        for i, project in enumerate(projects):
            print(f"{i + 1}. {project}\n")
            el.append(project)

    choice = int(input("Chose project number to modify: "))
    project_to_change = projects[choice - 1]
    print("If project variable is to be unchanged, just press Enter") 
    name = input("Project name: ")
    if name == "":
        name = project_to_change["name"]
    start = input("Project start date: ")
    if start == "":
        start = project_to_change["start"]
    finish = input("Project finish date: ")
    if finish == "":
        finish = project_to_change["finish"]
    progress = input("Project progress: ")
    if progress == "":
        progress = project_to_change["progress"]
    status = input("Project status: ")
    if status == "":
        status = project_to_change["status"]
    changed_project = {
        "name" : name,
        "start" : start,
        "finish" : finish,
        "progress" : progress,
        "status" : status
        }
    el.remove(project_to_change)
    el.append(changed_project)

    with open(ep_file, "w") as file:
        json.dump(el, file)

    start_menu()


# Project archiving
def archive_project(project_file, project_list, current_file, current_list, full_archive_file, full_archive_list):
    project_list.clear()
    current_list.clear()
    full_archive_list.clear()

    with open(project_file, "r") as file:
        projects = json.load(file)
        for i, project in enumerate(projects):
            print(f"{i + 1}. {project}\n")
            project_list.append(project)

    with open(current_file, "r") as file:
        projects = json.load(file)
        for project in projects:
            current_list.append(project)

    with open(full_archive_file, "r") as file:
        projects = json.load(file)
        for project in projects:
            full_archive_list.append(project)

    idx = int(input("Chose project number to archive: "))
    project_to_archive = project_list[idx - 1]

    project_list.remove(project_to_archive)
    with open(project_file, "w") as file:
        json.dump(project_list, file)

    current_list.append(project_to_archive)
    with open(current_file, "w") as file:
        json.dump(current_list, file)
        
    full_archive_list.append(project_to_archive)
    with open(full_archive_file, "w") as file:
        json.dump(full_archive_list, file)

    start_menu()
    