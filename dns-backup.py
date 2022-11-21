#!/usr/bin/python3
import pandas as ps
import json
import sys
import sys
import requests as req
import datetime

api1 = './api-key-local'
api2 = './api-key-external'
ip1 = '10.1.0.2:5380'
ip2 = '209.145.62.205:82'
file1 = './10.1.0.2-key'
file2 = './209.145.62.205-key'

def new_keys():

    server1 = [api1, ip1, file1]
    server2 = [api2, ip2, file2]

    hit_list = [server1, server2]

    for serverkey in hit_list:

        api_file = serverkey[0]
        ip_addr = str(serverkey[1])
        formatted_api = str(serverkey[2])

        with open(api_file) as j:
            api_data = json.load(j)

        with open(formatted_api, "w") as write_file:
            json.dump(api_data, write_file, indent=2)

def backups():

    now = datetime.datetime.now()
    timestamp = now.strftime("%d-%m-%Y")

    server1 = [ip1, file1]
    server2 = [ip2, file2]

    hit_list = [server1, server2]

    for server in hit_list:

        ip_addr = str(server[0])
        api_key = str(server[1])

        with open(api_key) as j:
            api_data = json.load(j)

            dns_token = str(api_data['token'])
            dns_username = str(api_data['username'])
            url = f"http://{ip_addr}/api/settings/backup?token={dns_token}&blockLists=true&logs=true&scopes=true&stats=true&zones=true&allowedZones=true&blockedZones=true&dnsSettings=true&logSettings=true&authConfig=true"
            file = req.get(url, allow_redirects=True)
            download_name = f"./data/{timestamp}-{ip_addr}.zip"
            print(open(download_name, 'wb').write(file.content))
        # print(dns_username)



arguments = int(len(sys.argv))

if arguments == 2:
    function = str(sys.argv[1])
    if function == "backups":
        backups()
    else:
        a=1
