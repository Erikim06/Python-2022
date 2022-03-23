from adventurelib import *

Room.items = Bag()

carge = Room("""Where the car is.""")

docking = Room("""The room for farming ducks""")

hallway = Room("""Dark old hallway""")

bridge = Room("""Where everyone gathers""")

quarters = Room("""Where people sleep""")

mess_hall = Room("""Where people eat something""")

escape_pods = Room("""Where people escape the spaceship""")
 
space = Room(""" 
	You are drifting in space. It feels very cold.
	A slate-blue spaceship sits completely silently to your left,
	its airlock open and waiting.
	""")

spaceship = Room("""
	The bridge if the spceship is shiny and white, with thousands 
	of small, red, blinking lights.
	""")

spaceship.east = hallway
spaceship.south = quarters
hallway.east = bridge
hallway.north = cargo
hallway.south = mess_hall
cargo.east = docking
bridge.south = escape_pods



Item.description = ""

knife = Item("a dirty knife","knife")
knife.description = "the knife has a dull sheen to it but it looks rather sharp."

red_keycard = Item("a red keycard","keycard","red card","red carde")
red_keycard.description = "It's a red keycard"

key = item("a silver key")
key.description = "normal key"

current_room = space
inventory = Bag()

mess_hall.items.add(red_keycard)
cargo.items.add(knife)
Quarters.items.add(key)

@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exists():
		current_room = current_room.exit(direction)
		print(f"you go {direction}.")
		print(current_room)


@when("look")
def look():
	print(cuurent_room)
	print(f"There are exits to the {current_room.exits()}.")
	if len(current_room.items) > 0:
	    print("You also see:")
	    for item in cuurent_room.items:
	    	print(item)


current_room = space
@when("enter airlock")
@when("enter spaceship")
@when("enter ship")
def enter_spaceship():
	global current_room
	if current_room is not space:
		say("There is no airlock here")
		return
	else:
		current_room = spaceship
		print("""you have yourself into the spaceship and
			slam you hand on the button to close the door.
			""")
		print(current_room)

@when("brush teeth")
@when("brush")
@when("clean teethy")
def brush_teeth():
    print("You brush your teeth")

@when("comb hair")
@when("comb")
def comb_hair():
	say("""
		 you brush your long flowing locks with
		 the gold hairbrush that you have selected from the 
		 in the red basket.
		 """)






def main():
	start()

if __name__ == '__main__':
	main()