import requests

url = "https://jsonplaceholder.typicode.com/posts/"

payload = {"id": [1, 2, 3], "userId":1}

responce = requests.get(url, params=payload)

responce_json = responce.json()

for i in responce_json:
  print(i , "\n")