#!/bin/python3

def drink(money):
	if money >500:
		return "You got a drink!"
	else:
		return "Not enough money!"

print(drink(400))
print(drink(600))

def alcohol(age,money):
	if (age > 18) and (money >500):
		return "You got a drink!"
	elif (age >18) and (money <500):
		return "Not enough money!"
	elif (age <18) and (money>500):
		return "Too young to drink"
	else:
		return "Too young and too poor!"

print(alcohol(19,600))
print(alcohol(19,400))
print(alcohol(17,600))
print(alcohol(17,400))
