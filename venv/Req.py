import requests
import json

data = {
  "id": 1,
  "category": {
    "id": 0,
    "name": "cat"
  },
  "name": "Basya",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 1,
      "name": "Basya"
    }
  ],
  "status": "available"
}
res = requests.post(f'https://petstore.swagger.io/v2/pet/', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, json=data)
print(res.status_code)
print(res.json())

res = requests.get( f'https://petstore.swagger.io/v2/pet/1', headers={'accept': 'application/json'})
print(res.status_code)
print(res.json())


data = {
  "id": 1,
  "category": {
    "id": 1,
    "name": "dog"
  },
  "name": "Rex",
  "photoUrls": [
    "string"
  ],
  "tags": [
    {
      "id": 1,
      "name": "Rex"
    }
  ],
  "status": "available"
}

res = requests.put(f'https://petstore.swagger.io/v2/pet/', headers={'accept': 'application/json', 'Content-Type': 'application/json'}, json=data)
print(res.status_code)
print(res.json())

res = requests.delete(f'https://petstore.swagger.io/v2/pet/1', headers={'accept': 'application/json'})
print(res.status_code)
print(res.json())

