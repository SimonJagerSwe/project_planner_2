# Imports
import json

# Project & archive files
pp_file = "projects_and_archives/programming_projects.json"
programming_projects = []
pa_file = "projects_and_archives/programming_archive.json"
programming_archive = []
ep_file = "projects_and_archives/everyday_projects.json"
everyday_projects = []
ea_file = "projects_and_archives/everyday_archive.json"
everyday_archive = []
fa_file = "projects_and_archives/full_archive.json"
full_archive = []

def initialize_project_lists():
    with open(pp_file, "r") as file:
        try:
            p_projects = json.load(file)
            for project in p_projects:
                programming_projects.append(project)
        except:
            print("Currently no programming projects available")
            pass

    with open(pa_file, "r") as file:
        try:
            p_archive = json.load(file)
            for project in p_archive:
                programming_archive.append(project)
        except:
            print("Currently no programming projects in archive")
            pass

    with open(ep_file, "r") as file:
        try:
            e_projects = json.load(file)
            for project in e_projects:
                everyday_projects.append(project)
        except:
            print("Currently no everyday projects available")
            pass
    
    with open(ea_file, "r") as file:
        try:
            e_achive = json.load(file)
            for project in e_achive:
                everyday_archive.append(project)
        except:
            print("Currently no everyday projects in archive") 
            pass

    with open(fa_file, "r") as file:
        try:
            f_archive = json.load(file)
            for project in f_archive:
                full_archive.append(project)
        except:
            print("Archive currently empty")
            pass

    return programming_projects, programming_archive, everyday_projects, everyday_archive, full_archive
