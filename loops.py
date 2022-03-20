print("Hi, welcome to the ice cream maker!")
order_complete = False
toppings_list = []
topping_count = 0
toppings_available = {"Vanilla", "strawberry", "chocolate", "sprintcles","nuts", "raisins", "chocolate source", "flake", "m&ms"}

while order_complete == False:
	topping = input(f"choose from this list of toppings. \n {toppings_available}\n")
	if topping_count >=6
	    print("order done")
	    order complete = True
	elif topping.lower() not in toppings_available:
		print("That is not available")
	elif topping.lower() in toppings_list:
		print("you already have that topping")
	else:
		print("Great, it's in the list")
		topping_count += 1
		toppings_list.append(topping)
print("Here are your toppings")
print(",". join(toppings_list))

print("\n")

