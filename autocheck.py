import requests
import json
from datetime import datetime
import csv
import sys

if len(sys.argv) > 1:
    if sys.argv[1] == 'update':
        with open('customer.csv') as file:
            csvreader = csv.reader(file)
            for row in csvreader:
                if 'NOK' in row[0]:
                    with open('header.json', 'r+', encoding='utf-8') as payload:
                        data = json.load(payload)
                        data['name'] = row[1]
                        birthdate = row[2].split("/")
                        data['birthDate'] = "{}. {}. {}.".format(birthdate[2], birthdate[1], birthdate[0])
                        data['phoneNumber'] = row[3]
                        data['email'] = row[4]
                        data['extraData'][0]['value'] = row[5]
                        payload.seek(0)
                        json.dump(data, payload, indent=4,ensure_ascii=False)
                        payload.truncate()
                    break

url = '<URL>'
with open('header.json', 'r+', encoding='utf-8') as payload:
    data = json.load(payload)
    now = datetime.now()
    dt_string = now.strftime("%Y/%m/%dT%H:%M:%S")
    data['timeSheet']['date'] = dt_string
    payload.seek(0)
    json.dump(data, payload, indent=4,ensure_ascii=False)
    payload.truncate()
    
with open('header.json', 'r+', encoding='utf-8') as payload:
    data=json.load(payload)
    #print(data)
    headers = {'content-type': 'application/json; charset=utf-8'}
    r = requests.post(url, data=json.dumps(data), headers=headers)
    print(r.json())
