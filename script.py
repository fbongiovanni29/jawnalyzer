import json
from collections import OrderedDict

# loads json and sets it to var data
with open('all-companies.json') as data_file:
        data = json.load(data_file)

# amount of companies in Job Jawn
amount_companies = len(data)

# declare for loop
skills = []

# Appends each technology to the skills array
for companies in data:
    for i in companies["technologies"]:
        skills.append(i)

# Organizes JSON as Key, Val
# Key === Skill
# Val === Times Listed
skill_json = ({i: skills.count(i) for i in skills})
# Orders by Value descending
skill_json = sorted(skill_json.items(), key=lambda x: x[1], reverse=True)
skill_json = OrderedDict(skill_json)
# Converts back to JSON
skill_json = json.dumps(skill_json, indent=4)

title_counter = 0
titles = []

# appends each title to titles array
for positions in data:
    for i in positions["positions"]:
        titles.append(i["title"])
        title_counter = title_counter + 1

title_json = ({i: titles.count(i) for i in titles})
# Orders by Value descending
title_json = sorted(title_json.items(), key=lambda x: x[1], reverse=True)
title_json = OrderedDict(title_json)
# Converts back to JSON
title_json = json.dumps(title_json, indent=4)
