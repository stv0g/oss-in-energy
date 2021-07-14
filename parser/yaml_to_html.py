#!/usr/bin/env python

import yaml
from oss_project import OpenSourceProject

with open("../projects.yaml", "r") as stream:
    try:
        data = yaml.safe_load(stream)
        for p in data["projects"]:
            project = OpenSourceProject.from_dict(p)
            print(project)

    except yaml.YAMLError as exc:
        print("Error: Invalid yaml file:")
        print(exc)
