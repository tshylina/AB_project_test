import json
from models.group import Group
import os.path
import random
import string
# import

cyr_symbol = ''.join([chr(l) for l in range(0x0400, 0x04FF) if chr(l).isprintable()])

def random_string(maxlen):
    length = random.randrange(1, maxlen)
    symbols = cyr_symbol + string.ascii_letters + string.digits + string.punctuation + " " * 10
    result = ""
    for  i  in range (length):
        result += random.choice(symbols)
    return result

print(random_string(255))

file_name = os.path.join(os.path.dirname(os.path.abspath(__file__)), "groups.json")


with open(file_name, encoding='utf8') as f:
    groups_list = [Group(**data) for data in json.load(f)]

    # groups_list = []
    # for data in group_data:
    #     g = Group(name=data["name"], header=data["header"], footer=data["footer"])
    #     groups_list.append(g)

    # print(groups_list)
# print(groups_list)
groups_list += [Group(name=random_string(20), header=random_string(50), footer=random_string(150))
for _ in range (5)]