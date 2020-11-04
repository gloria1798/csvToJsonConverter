#import packages to read csv
import csv, json

csvFilePath = 'flare_input.csv'
jsonFilePath = 'flare_output.json'

# read csv file and add to data 
data = {}
with open(csvFilePath, 'r') as csvFile:
    csvReader = csv.DictReader(csvFile)
    for rows in csvReader:
        id = rows['id']
        data[id] = rows

# create new json file and write data on it
with open(jsonFilePath, 'w') as jsonFile:
    # make it more readable and pretty
    jsonFile.write(json.dumps(data, indent=4))

print (jsonFile)

