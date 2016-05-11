import json
from collections import OrderedDict

# loads json and sets it to var data
with open('all-companies.json') as data_file:
    data = json.load(data_file)

# amount of companies in Job Jawn
amount_companies = len(data)

skills = []
types = []
titles = []
title_counter = 0

# Appends each technology to the skills array
for companies in data:
    for i in companies["technologies"]:
        skills.append(i)


for companies in data:
    for i in companies["type"]:
        types.append(i)

for positions in data:
    for i in positions["positions"]:
        titles.append(i["title"])
        title_counter = title_counter + 1

# Organizes data into JSON


def json_formatter(json_name):
    # Organizes JSON as Key, Val
    formatted = ({i: json_name.count(i) for i in json_name})
    # Orders by Value descending
    formatted = sorted(formatted.items(), key=lambda x: x[1], reverse=True)
    formatted = OrderedDict(formatted)
    # Converts back to JSON
    formatted = json.dumps(formatted, indent=4)
    print formatted
    return

json_formatter(skills)
json_formatter(types)
json_formatter(titles)
