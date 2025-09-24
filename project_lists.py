# Imports
import json

# Project & archive files
pp_file = "programming_projects.json"
programming_projects = []
pa_file = "programming_archive.json"
programming_archive = []
ep_file = "everyday_projects.json"
everyday_projects = []
ea_file = "everyday_archive.json"
everyday_archive = []
fa_file = "full_archive.json"
full_archive = []

def initialize_project_lists():
    with open(pp_file, "r") as file:
        p_projects = json.load(file)
        for project in p_projects:
            programming_projects.append(project)

    with open(pa_file, "r") as file:
        pa = json.load(file)
        for project in pa:
            programming_archive.append(project)
   
    with open(ep_file, "r") as file:
        e_projects = json.load(file)
        for project in e_projects:
            everyday_projects.append(project)
    
    with open(ea_file, "r") as file:
        ea = json.load(file)
        for project in ea:
            everyday_archive.append(project)

    with open(fa_file, "r") as file:
        fa = json.load(file)
        for project in fa:
            full_archive.append(project)

    return programming_projects, programming_archive, everyday_projects, everyday_archive, full_archive
