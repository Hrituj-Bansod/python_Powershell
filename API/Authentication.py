import requests

payload = {'username' : 'Hrituj' , 'password' : 'pass'}

r = requests.post('https://httpbin.org/post' , data=payload)

#print(r.text)

r1 = requests.post('https://httpbin.org/basic-auth/Hrituj/pass,auth=("Hrituj","pass")')

print(r.text)