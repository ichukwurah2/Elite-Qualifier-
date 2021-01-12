​import random
import time

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