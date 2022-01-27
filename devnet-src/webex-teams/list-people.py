# Fill in this file with the people listing code from the Webex Teams exercise

import requests
import json
access_token = 'NmQ0OGRkYWUtODI5MC00YWQ0LTgwYTUtZmE2YWIzMTc2ZDllNzMxY2VlMzctM2E3_P0A1_ffe50b97-2b4a-4965-8373-9822eafeddfd'
url = 'https://webexapis.com/v1/people'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params = {'email': 'Mahmoud.shikhwis@student.odisee.be' }
res = requests.get(url, headers=headers, params=params)
print(json.dumps(res.json(), indent=4))



person_id = 'Y2lzY29zcGFyazovL3VzL1BFT1BMRS83N2E2MGU3ZS1lOGFkLTQ3ZTAtYTI4NC0xNTBmZWI5MGJmNjI'
url = 'https://webexapis.com/v1/people/{}'.format(person_id)
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))