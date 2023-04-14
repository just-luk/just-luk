import csv
import os
import json
dir_list = os.listdir('data')
with open('data.json', 'r') as r:
    parameters = json.loads(r.read())
csv_files = []
for file in dir_list:
    if file[-1] == 'v':
        csv_files.append('data/' + file)

all_data = {}
with open(csv_files[0], newline='', encoding='latin1') as c:
    temp = csv.DictReader(c, delimiter=',')
    for row in temp:
        unit_id = row['UNITID']
        all_data[unit_id] = []

for file in csv_files:
    print(f'reading {file}')
    csv_name = file[5:-4]
    with open(file, newline='', encoding='latin1') as csvfile:
        data_map = csv.DictReader(csvfile, delimiter=',')
        for row in data_map:
            for param in parameters[csv_name]:
                all_data['UNITID'].append(row[param])
            


            