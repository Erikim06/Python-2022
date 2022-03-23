from adventurelib import *

@when ("go DIRECTION")
def travel(direction):
	global current_room
	if direction in current_room.exists():
		current_room = current_room.exit(direction)
		print(f"you go {direction}.")
		print(current_room)







def main():
	start()

if __name__ == '__main__':
	main()