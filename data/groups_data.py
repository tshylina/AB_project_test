import json
from models.group import Group

with open("groups.json", encoding='utf8') as f:
    group_data = json.load(f)
    groups_list = [Group(name=data["name"], header=data["header"], footer=data["footer"])
                    for data in group_data]
    # groups_list = []
    # for data in group_data:
    #     g = Group(name=data["name"], header=data["header"], footer=data["footer"])
    #     groups_list.append(g)

    # print(groups_list)
        print(groups_list)