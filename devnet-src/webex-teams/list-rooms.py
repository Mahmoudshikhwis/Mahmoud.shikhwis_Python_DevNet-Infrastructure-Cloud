# Fill in this file with the rooms/spaces listing code from the Webex Teams exercise

import requests
access_token = 'NmQ0OGRkYWUtODI5MC00YWQ0LTgwYTUtZmE2YWIzMTc2ZDllNzMxY2VlMzctM2E3_P0A1_ffe50b97-2b4a-4965-8373-9822eafeddfd'
url = 'https://webexapis.com/v1/rooms'
headers = {
 'Authorization': 'Bearer {}'.format(access_token),
 'Content-Type': 'application/json'
}
params={'max': '100'}
res = requests.get(url, headers=headers, params=params)
print(res.json())
