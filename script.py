import json

with open('all-companies.json') as data_file:
        data = json.load(data_file)

print len(data)

counter = []

for companies in data:
    for i in companies["technologies"]:
        counter.append(i.lower())

print {i:counter.count(i) for i in counter}
#    for technologies in companies["technologies"]:
#        print technologies["technologies"]
#        print companies[technologies]["technologies"]
        

for companies in data:
    for i in companies["technologies"]:
        counter.append(i)
