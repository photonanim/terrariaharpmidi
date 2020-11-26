import csv
import json

csvFilePath = 'path'
jsonFilePath = 'path'

data = {}

print("I'm not hallucinating.")
id = 0
with open(csvFilePath) as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        data[id] = rows
        id += 1
print(data)
with open(jsonFilePath, 'w') as x:
    x.write(json.dumps(data,indent=4))
