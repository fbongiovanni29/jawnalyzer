import json
from collections import OrderedDict

# loads json and sets it to var data
with open('all-companies.json') as data_file:
    data = json.load(data_file)

technologies = []
types = []
titles = []
jobLocation = []
employmentType = []
my_json = []

# prints amount of remote positions
remote = json.dumps(data).count('"remote": true,')
# amount of companies in Job Jawn
amount_companies = len(data)


def json_int(key, val):
    aDict = {}
    aDict[key] = val
    my_json.append(aDict)

json_int("remote", remote)
json_int("companies", amount_companies)


def json_loop(key, array, position, my_json):
    # Loops through json
    for companies in data:
        for i in companies[key]:
            # Checks nesting
            if position is None:
                array.append(i)
            else:
                array.append(i[position])
    # Organizes into JSON as Key, Val
    formatted = ({i: array.count(i) for i in array})
    # Orders by Value descending
    formatted = sorted(formatted.items(), key=lambda x: x[1], reverse=True)
    formatted = OrderedDict(formatted)
    # Converts back to JSON
    json_int(key, formatted)
    return

json_loop("technologies", technologies, None, my_json)
json_loop("type", types, None, my_json)
json_loop("positions", jobLocation, "jobLocation", my_json)
json_loop("positions", titles, "title", my_json)
json_loop("positions", employmentType, "employmentType", my_json)
print(json.dumps(my_json, indent=4))
