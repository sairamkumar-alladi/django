import requests
import json

BASE_URL = 'http://127.0.0.1:8000/studentapi2'

def get_data(id=None):
    url = BASE_URL  # Use a local variable for the URL
    if id is not None:
        url = f'{url}/{id}'
    
    r = requests.get(url=url)
    
    # Ensure we have a successful response
    if r.status_code == 200:
        resp_data = r.json()
        print(resp_data)
    else:
        print(f'Error: {r.status_code}, Response: {r.text}')

get_data()

def post_data():
    data = {
        'name' : 'Ramu',
        'roll' : 201,
        'city' : 'Kurnool'
    }

    json_data = json.dumps(data)
    r = requests.post(url=BASE_URL, data= json_data)
    data = r.json()

    print(data)

post_data()

def update_data():
    data = {
        'id' : 1,
        'name' : 'sai',
        'roll' : 200,
        'city' : 'Nirmal'
    }

    json_data = json.dumps(data)
    r = requests.put(url=BASE_URL, data= json_data)
    data = r.json()

    print(data)

# update_data()
def delete_data():
    data = {
        'id' : 3,
    }

    json_data = json.dumps(data)
    r = requests.delete(url=BASE_URL, data= json_data)
    data = r.json()

    print(data)

# delete_data()

