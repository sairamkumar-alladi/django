import requests
import json

URL = 'http://127.0.0.1:8000/api/createstudent'

data = {
    'name' : 'Raj',
    'roll' : 102,
    'address' : 'Hyd'
}

json_data = json.dumps(data)
r = requests.post(url=URL, data= json_data)
data = r.json()

print(data)