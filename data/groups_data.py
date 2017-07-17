import json
from models.group import Group
import os.path

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "groups.json")

print(file_name)

with open("groups.json", encoding='utf8') as f:
    groups_list = [Group(**data) for data in json.load(f)]

    # groups_list = []
    # for data in group_data:
    #     g = Group(name=data["name"], header=data["header"], footer=data["footer"])
    #     groups_list.append(g)

    # print(groups_list)
print(groups_list)