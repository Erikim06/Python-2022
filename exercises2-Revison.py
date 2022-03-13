"""
ice_cream = int(input("how many icecreams do you want?")) #1
if ice_cream >20:
	print("There isn't enough ice cream stock")
elif ice_cream <20:
	print("Sure!")

how_far = int(input("how far would you like to travel?")) #2
if how_far >200:
    print("fill up the petrol before you travel")
elif how_far <200:
    print("goodgood")

user_age = int(input("what is your age?")) #3
if user_age >= 18:
    print("you are an adult!")
elif user_age < 18:
	print("you are a kid")

user_movie = input("What is your favourite movie?") #4
if user_movie =="Lord of the king":
    print("you have exellent taste!")
else:
    print("Lord of the kings is better")


user_heard =input("have you heard the tale of Darvh Plagueis the Wise?") #5
if user_heard == "yes":
	print(" You must be a fan")
else:
	print("tale of Darvh Plagueis the Wise")

Director = input("who is the director of Passion of the Christ?")#6
if Director == "Mel Gibson":
	print("Correct")
else:
	print("unlucky")
"""
score = 0
city = input("What is a capital city of France?") #7
if city == "Paris" or city == "paris":
	print("well done")
	score = score + 1
else:
	print("wrong")


ocean = input("What is the biggest ocean in the world?")
if ocean == "Pacific Ocean" or ocean == "Pacific ocean" or ocean == "pacific ocean":
    print("Correct")
    score = score + 1
else: 
	print("No")

days = int(input("How many days in one year?"))
if days == "365":
	print("Nice")
	score = score + 1
else:
	print("Unlucky")

print("TRUE OR FALSE")
sheep = input("There are more sheeps in New Zealand than NZ human population")
if sheep == "TRUE" or sheep == "True" or sheep == "true":
    print("Good")
    score = score + 1
else:
	print("incorrect")

olympic = input("how often does the olymic happens?")
if olympic == "4" or olympic == "4 years" or olympic == "4 Years":
	print("You are right")
	score = score + 1
else:
	print("Hard luck")


print("your score is",score)
print(f"you got, %s questions right!"%score)





