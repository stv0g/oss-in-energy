#!/usr/bin/env python

import yaml
from oss_project import OpenSourceProject
from tabulate import tabulate

with open("../projects.yaml", "r") as stream:
    try:
        data = yaml.safe_load(stream)
        proj_list = []
        for p in data["projects"]:
            project = OpenSourceProject.from_dict(p)
            print(project)
            proj_list.append(project.to_list())
        with open("table.html", 'w') as htmlfile:
            htmlfile.write(tabulate(proj_list, tablefmt='unsafehtml', headers=OpenSourceProject.list_headers()))

    except yaml.YAMLError as exc:
        print("Error: Invalid yaml file:")
        print(exc)
