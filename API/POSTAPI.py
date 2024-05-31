import requests

Data = {
    "userID": 123,
    "title": "POST Request",
    "body": "Body is added here"
}

url = "https://jsonplaceholder.typicode.com/posts"
responce = requests.post(url, json=Data)
responce_json = responce.json()
print(responce_json)

print(responce.status_code)