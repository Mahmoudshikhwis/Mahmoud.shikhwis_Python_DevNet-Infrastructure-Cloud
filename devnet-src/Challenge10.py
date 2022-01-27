from textwrap import indent
import requests
import json
requests.packages.urllib3.disable_warnings()

IP_HOST = "192.168.56.101"
Username = "cisco"
Password = "cisco123!"
URL = f'https://{IP_HOST}:443/restconf/data/Cisco-IOS-XE-native:native/logging/monitor/severity'
HEADER = {'Accept':'application/yang-data+json'}
basicauth = (Username, Password)

result = requests.options(URL, auth=basicauth, headers=HEADER, verify=False)

print(result.url[:5], result.raw.version, result.status_code, result.reason)

print(json.dumps(dict(result.headers), indent=2))

