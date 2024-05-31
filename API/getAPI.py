import requests

url = "https://jsonplaceholder.typicode.com/posts/1"

responce = requests.get(url)

responce_json = responce.json()
print(responce_json)

print(responce.status_code)