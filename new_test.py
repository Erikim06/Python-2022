from adventurelib import *

@when("brush teeth")
@when("brush")
@when("clean teethy")
def brush_teeth():
    print("You brush your teeth")

@when("comb hair")
@when("comb")
def comb+_hair():
	say("""
		 you brush your long flowing locks with the gold hairbrush that you have selected from the in the red basket.""")

def main():
	start()

if __name__ == '__main__':
	main()