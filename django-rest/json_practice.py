import json
details = {'Name':'Sai', 'Age':28}
json_data = json.dumps(details)
print(json_data)


import json
json_string = '{"Name": "Sai", "Age": 28}'
json_data = json.loads(json_string)
print(json_data)

