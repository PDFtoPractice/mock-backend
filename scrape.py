import csv
import json

data = []

output = open('data.json', 'w+')

with open('data.csv') as f:
    for row in csv.DictReader(f):
        data.append(row)

json_data = json.dumps(data)

output.write(json_data)
