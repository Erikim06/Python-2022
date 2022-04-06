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


room1.east = room2
room2.north = corridor
room2.south = kitchen
room2.east = room3
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
master_room.items.add(driver)
prison.items.add(hammer)
room4.items.add(flare_gun)


if current_room = room2 and item = key1

current_room = room1
inventory = Bag()




@when("go east")
def enter_room():
	global current_rooms
	if current_room is not room1:
		print("These is no room2")
		return
	elif key1 is not in player_inventory:
	    print("you need the key1 to enter the room2")
	    return
	else:
		current_room = room2
		print("You unlocked the door")
		print(current_room)


@when("enter living room")
@when("go to living room")
@when("go inside the living room")
@when("go to the living room")
def enter_room():
	global current_rooms
	if current_room is not corridor or prison:
		print("There is no living room")
		return
	elif key1 is not in player_inventory: #sup eric - dominik
	    print("you need the key1 to enter the living room")
	    return
	else:
		current_room = living_room
		print("You unlocked the door")
		print(current_room)

@when("enter prison")
@when("go to prison")
@when("go to the prison")
@when("go inside the prison")
def enter_room():
	global current_rooms
	if current_room is not master_room or living_room:
		print("These is no prison arounfd you")
	elif key2 is not in player_inventory:
		print("You need the key2 to enter the prison")
	else:
		current_room = prison
		print("You entered the prison")
		print(current_room)






front_door = 30

if front_door == 0:
	print("You have escaped the house")
	


@when("use hammer")
def escape(house):
	if hammer in player_inventory and current_room == corridor and front_door ==30:
		print("You have damaged the front_door but not quite there.")
		front_door = 20
	elif hammer in player_inventory and current_room == corridor and front_door ==20:
		print("Neally there.")
		front_door = 10
	else hammer in player_inventory and current_room == corridor and front_door ==10:
		print("You've smashed the front door! You can now use the flare_gun.")
		front_door = 0
	

@when("use driver")
def escape(house):
	if driver in player_inventory and current_room == corridor and front_door ==30:
		print("You have loosened the front door, but not there yet.")
		front_door = 20
	elif driver in player_inventory and current_room == corridor and front_door ==20:
		print("You are close")
		front_door = 10
	else driver in player_inventory and current_room == corridor and front_door ==10:
		print("You've smashed the front door! You can now use the flare_gun.")
		front_door = 0
	

@when("use chain saw")
def escape(house):
	if chain saw in player_inventory and current_room == corridor and front_door ==30:
		print(" Little bit more work to do.")
		front_door = 20
	elif chain saw in player_inventory and current_room == corridor and front_door ==20:
		print("You are close")
		front_door = 10
	else chain saw in player_inventory and current_room == corridor and front_door ==10:
		print("You've smashed the front door! You can now use the flare_gun.")
		front_door = 0
	

@when("use flare gun")
@when("use the flare gun")
def escape(island):
	if front door == 0:
		print("GAME OVER")
		print("You have escaped the island!")
	else:
		print("You can't use flare gun")




@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")
	else:
		print(f"you don't see a {item}")`

@when ("go DIRECTION")
def travel(direction):
   global current_room

	if current_room == room1 and direction == 'east' and key1 is in player_inventory:
		print("You have entered the room2.")

	if current_room == corridor and direction == 'east' and key1 is in player_inventory:
		print("You have entered the room4.")

	if current_room == prison and direction == 'west' and key1 is in player_inventory:
		print("You have entered the room4.")





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

@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
	if item in current_room.items:
		t = current_room.items.take(item)
		inventory.add(t)
		print(f"You pick up the {item}")brush
	else:
		print(f"you don't see a {item}")


print()

def main():
	start()

if __name__ == '__main__':
	main()