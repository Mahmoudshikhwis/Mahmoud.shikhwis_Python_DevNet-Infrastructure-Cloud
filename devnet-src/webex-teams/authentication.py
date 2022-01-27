# Fill in this file with the authentication code from the Webex Teams exercise
import requests
import json
access_token = 'NmQ0OGRkYWUtODI5MC00YWQ0LTgwYTUtZmE2YWIzMTc2ZDllNzMxY2VlMzctM2E3_P0A1_ffe50b97-2b4a-4965-8373-9822eafeddfd'
url = 'https://webexapis.com/v1/people/me'
headers = {
 'Authorization': 'Bearer {}'.format(access_token)
}
res = requests.get(url, headers=headers)
print(json.dumps(res.json(), indent=4))