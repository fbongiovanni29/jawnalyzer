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


def json_loop(key, array):
    for companies in data:
        for i in companies[key]:
            array.append(i)

json_loop("technologies", technologies)
json_loop("type", types)


def postions_json_loop(key, array):
    for positions in data:
        for i in positions["positions"]:
            array.append(i[key])

postions_json_loop("jobLocation", jobLocation)
postions_json_loop("title", titles)


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

json_formatter(technologies)
json_formatter(types)
json_formatter(jobLocation)
json_formatter(titles)
