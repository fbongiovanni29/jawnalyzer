import json
import jsonpickle
from collections import OrderedDict

with open('all-companies.json') as data_file:
        data = json.load(data_file)

#print len(data)

counter = []

for companies in data:
    for i in companies["technologies"]:
        counter.append(i)

my_json = ({i:counter.count(i) for i in counter})
my_json = OrderedDict(sorted(my_json.items(), key=lambda x: x[1], reverse=True))
my_json = json.dumps(my_json, indent=4)
#print my_json

title_counter = 0

for positions in data:
    for position in positions["positions"]:
        print position["title"]
        title_counter = title_counter + 1

print 

#print title_counter
