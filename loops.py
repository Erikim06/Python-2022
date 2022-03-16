topping_count=0
while topping_count==false
      topping = input("Add a topping")
      topping_count= (topping_count+1)
      


toppings_available=['vanilla', 'strawberry', 'chocolate', 'sprinkles', 'nuts', 'raisins', 'chocolate sauce', 'flake','m&ms']
print(toppings_available)
print("you are only able to order the toppings from the list")
toppings= input("Pick from the list")
if topping== "":
	print("good choice")
else:
	print("not available")

