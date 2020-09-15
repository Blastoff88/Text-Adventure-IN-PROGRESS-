#This is our code project. We still do not know the name of it.....

import random
import time
from random import randint

print("This was made by THE NAME OF OUR GAME COMPANY")
time.sleep(1)
answer = input("Are you ready to start your journey? (y/n)\n")
if answer == "y":
  print("Nice.")
  time.sleep(1)
  assistant = input("Hello... I am (type my name here)\n")
  answer = input("Nice name! " + assistant + " sounds good on me, doesn't it? (y/n)\n")
  if answer == "n":
    print("How rude.")
  elif answer == "y":
    print("Thanks!")
  else:
    print("????????")
  time.sleep(1)
  you = input("Now, I want to know your name. Type it here, please:\n")
  print(you + ", I like that name.")
  time.sleep(1)
  print("Alright, let's start our journey!")
  time.sleep(1)
  print("There is a small town far away from here, and it is ruled by an evil king.")
  time.sleep(1)
  king = input("What was his name again?\n")
  print("Oh yeah.")
  time.sleep(1)
  print("Anyway, " + king + " is the king of the village, and he is planning to take over the world.")
  time.sleep(1)
  print("This village is thousands of miles away, and we have to get there as soon as possible.")
  time.sleep(1)
  route = input(you + ", there are three routes we can take.\nOne leads to a car dealership, so we can get to the village faster.\nAnother leads to a weapons store, where we can get some weapons.\nThe last one leads to the wise man, where we can gather wisdom.\nThese are all good choices, but we can only pick one. Where should we go to?\n(the car dealership, the weapons store, or the wise man.. remember to type in all lowercase.)")
  if route == "the car dealership":
    print("You go to the car dealership. The smell of new car overwhelms you, so you faint.")
    time.sleep(1)
    print("When you wake up, you find yourself in the backseat of the car with " + assistant + " driving.")
    time.sleep(1)
    print(assistant + " - We are here. The village we've been looking for!")
    time.sleep(1)
    print("You and " + assistant + " walk up to meet King " + king + ".")
    time.sleep(1)
    print("King " + king + " - Well, well, well, it looks like " + you + " and " + assistant + " are here to confront me. Guess what? You don't have a weapon! You silly fools picked the faster route over the precision route. Guards, take them away!")
    time.sleep(1)
    print("You and " + assistant + " are put in prison and are not able to escape.\nYou lost")
  elif route == "the weapons store":
    print("You walk to the weapons store where you find many assortments of weapons.")
    time.sleep(1)
    print("The cashier asks you if you want to buy a weapon.")
    time.sleep(1)
    print("You say yes, and the cashier likes what you want to buy.")
    weapon = input("What would you like to buy?\n")
    print("Cashier - Ah, the world famous " + weapon + ", a classic. Nice choice!")
    print("You are gifted the " + weapon + "!")
  elif route == "the wise man":
    print("You walk to the wise man.")
    time.sleep(1)
    print("Wise Man - My advice is that you choose another option.")
  else:
    print("You are too confusing for me. I am going to find another adventure partner.")
elif answer == "n":
  print("Okay, come back when you are ready.")
else:
  print("???????????")
