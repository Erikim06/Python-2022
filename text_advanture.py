from adventurelib import *

Room.items = Bag()

room1 = Room("""You are awake in this bedroom, it's old, dark abondened room. You can get the key in this room """)
room2 = Room("""The room2 is locked. You have to use the item to unlock it. When you get there you may get chain saw """)
kitchen = Room("""The kitchen is is very simple and eveything is dark, you can get the key there.""")
room3 = Room("""The room3 is very small and there are nothing in there.""")
room4 = Room("""The room4 is a living room and you need the key from the Room1 to open the secret room""")
corridor = Room("""Corridor is where the front door is, get all the items and try to unlock.""")
prison = Room("""The prison is just horrible, there are bonds everywhere and the weapons. You can get the hammer """)
master_room = Room("""master room is look alright and you can get the driver from there""")



room2.north = corridor
room2.south = kitchen
kitchen.east = master_room
master_room.north = prison
prison.west = room4
room4.west = corridor


Item.description = ""

key1 = Item("Shiny silver key")
key1.description = "You use it to escape the first room and to unlock the secret room."

key2 = Item("Rust key")
key2.description = "You use it to unlock the prison"

driver = Item("Normal driver")
driver.description = "The driver is to help you to unlock the front door. "

hammer = Item("The wood hammer")
hammer.description = "The hammer is to unlock the front door."

chain_saw = Item("The chain saw")
chain_saw.description = "it is for unlock the front door."

flare_gun = Item("Flare gun")
flare_gun.description= "You have to shoot the flare gun for help after you escape the house."


room1.items.add(key1)
room2.items.add(chain_saw)
kitchen.items.add(key2)
master_room.add(driver)
prison.items.add(locked)
room4.add(flare_gun)


if current_room = room2 and item = key1

current_room = space
inventory = Bag()


@when("use chain saw")
@when("use driver")
def escape(house):
	if current_room == corridor:
		chain_saw or driver in inventory
		print("You succesed to escape!")
	else:
		print("You can't use it")



@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"you don't see a {item}")

@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exits():
		current_room = current_room.exit(direction)
		print(f"you go {direction}.")
		print(current_room)


@when("look at ITEM")
@when("My ITEM")
@when("my ITEM")
def look_at(item):
	if item in inventory:
		t = inventory.find(item)
		print(t.description)
	else:
		print(f"you aren't carrying an {item}")

@when("inventory")
@when("show inventory")
@when("what is in my pocket")
def player_inventory():
	print("You are carrying")
	for item in inventory:
		print(item)


print()

def main():
	start()

if __name__ == '__main__':
	main()