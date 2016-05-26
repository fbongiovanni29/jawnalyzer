import json
import glob
from collections import OrderedDict
from itertools import groupby


# Assigns Key: Val and appends to array
def json_int(job_json, key, val):
    aDict = {}
    aDict[key] = val
    job_json.update(aDict)


# Extracts necessary JSON data and formats properly
def json_loop(data, key, array, position, job_json):
    nu_array = []
    # Loops through json
    for companies in data:
        for i in companies[key]:
            # Checks nesting
            if position is None:
                nu_array.append(i)
                d = {"type": i}
                d.update({'amount': nu_array.count(i)})
                array.append(d)
            else:
                nu_array.append(i[position])
                d = {"type": i[position]}
                d.update({'amount': nu_array.count(i[position])})
                array.append(d)
        array = sorted(array, key=lambda k: k['amount'], reverse=True)
        horray = []
        booray = []
        for i in array:
            if i["type"] not in horray:
              horray.append(i["type"])
              booray.append(i)
    array = booray
    formatted = booray
    if key is "positions":
        key = position
    json_int(job_json, key, array)
    return



def load_job_json(filename):
    job_json = {}
    technologies = []
    types = []
    titles = []
    jobLocation = []
    employmentType = []

    print "writing " + filename
    with open(filename) as data_file:
        data = json.load(data_file)
    # prints amount of remote positions
    remote = json.dumps(data).count('"remote": true,')
    # amount of companies in Job Jawn
    amt_companies = len(data)
    amt_nil_tech = json.dumps(data).count('"technologies": [],')
    amt_tech = amt_companies - amt_nil_tech
    print amt_tech

    json_loop(data, "technologies", technologies, None, job_json)
    json_loop(data, "type", types, None, job_json)
    json_loop(data, "positions", jobLocation, "jobLocation", job_json)
    json_loop(data, "positions", titles, "title", job_json)
    json_loop(data, "positions", employmentType, "employmentType", job_json)
    json_int(job_json, "remote", remote)
    json_int(job_json, "companies", amt_companies)
    json_int(job_json, "amt_technologies", amt_tech)
    with open("analyzed/" + filename[+5:], 'w') as outfile:
        json.dump(job_json, outfile, indent=4)


# loads json and sets it to var data
for filename in glob.iglob('json/*.json'):
    load_job_json(filename)
