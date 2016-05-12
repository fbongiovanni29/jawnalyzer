import json
import glob
from collections import OrderedDict

technologies = []
types = []
titles = []
jobLocation = []
employmentType = []
job_json = []


# Assigns Key: Val and appends to array
def json_int(key, val):
    aDict = {}
    aDict[key] = val
    job_json.append(aDict)


# Extracts necessary JSON data and formats properly
def json_loop(key, array, position, job_json):
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
    # if nested inside of positions
    if key is "positions":
        key = position
    json_int(key, formatted)
    return

# loads json and sets it to var data
for filename in glob.iglob('json/*'):
    with open(filename) as data_file:
        data = json.load(data_file)

    # prints amount of remote positions
    remote = json.dumps(data).count('"remote": true,')
    # amount of companies in Job Jawn
    amount_companies = len(data)

    json_loop("technologies", technologies, None, job_json)
    json_loop("type", types, None, job_json)
    json_loop("positions", jobLocation, "jobLocation", job_json)
    json_loop("positions", titles, "title", job_json)
    json_loop("positions", employmentType, "employmentType", job_json)
    json_int("remote", remote)
    json_int("companies", amount_companies)
    with open("analyzed/" + filename[+5:], 'w') as outfile:
        json.dump(job_json, outfile, indent=4)
