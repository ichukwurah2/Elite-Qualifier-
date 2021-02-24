​import random
import requests, sys, webbrowser, bs4
import time

res = requests.get('http://google.com/search?q='+'.join(sys.argv[1:]))
res.raise_for_status()

soup = bs4.BeatifulSoup(res.text, "html.parser")
LinkElements = soup.Select('.r a')
LinkToOpen = min(5, len(LinkElements))
for i in range(linkToOpen):
    webbrowser.open('http://google.com'+LinkElements)

name = input("Hello, what is your name? ")

time.sleep(2)
print("Hello " + name)

feeling = input("How are you today? ")
​​​time.sleep(2)

​if "great" in feeling:
    print("I'm feeling great")
else:
    print("I'm so sorry about that!")

​time.sleep(2)
favcandy = input("What is your favourite candy? ")
candy = ["twix", "Hersey", "Jolly Ranchers"]

time.sleep(2)
print("My favourite cabdy is " + random.choice(candy))