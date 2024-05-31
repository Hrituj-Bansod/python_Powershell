import requests

r = requests.get('https://xkcd.com/353/')

#print(help(r))


r1 = requests.get('https://imgs.xkcd.com/comics/python.png')

with open('IMG.png' , 'wb')as f:
    f.write(r1.content)