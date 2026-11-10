import random

print ("Welcome to 'whose wallet?' ")
print ("You will give me a list of names, and I will pick a person to pay ")

names = input("If you are ready, enter the names separated by a comma ").split(", ")

print (f"Please ask {random.choice(names) } to take out his wallet, dinner is on him.")