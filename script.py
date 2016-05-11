import json
from collections import OrderedDict

# loads json and sets it to var data
with open('all-companies.json') as data_file:
    data = json.load(data_file)

# amount of companies in Job Jawn
amount_companies = len(data)

# prints amount of remote positions
remote = json.dumps(data).count('"remote": true,')

technologies = []
types = []
titles = []
jobLocation = []
title_counter = 0


def json_loop(key, array, position):
    for companies in data:
        for i in companies[key]:
            if position is None:
                array.append(i)
            else:
                array.append(i[position])
    # Organizes data into JSON
    # Organizes JSON as Key, Val
    formatted = ({i: array.count(i) for i in array})
    # Orders by Value descending
    formatted = sorted(formatted.items(), key=lambda x: x[1], reverse=True)
    formatted = OrderedDict(formatted)
    # Converts back to JSON
    formatted = json.dumps(formatted, indent=4)
    print formatted
    return

json_loop("technologies", technologies, None)
json_loop("type", types, None)
json_loop("positions", jobLocation, "jobLocation")
json_loop("positions", titles, "title")
