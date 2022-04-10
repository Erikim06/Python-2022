from adventurelib import *

Room.items = Bag()

room1 = Room("""This is room1.\nYou are awake in this bedroom,\nit's old, dark abondened room. You can get the key in this room. You can exit the room if you go east but they key is required.""")
room2 = Room("""This is room2.\nGet chain saw to lock the front door in the corridor. You can go to the any direction in this room. """)
kitchen = Room("""This is Kitchen.\nThe kitchen is very simple and quite dark, you can get the rust key there. Get the rust key in that room to unlock the prison.""")
room3 = Room("""This is room3.\nThe room3 is very small and there are nothing.""")
room4 = Room("""This is room4.\nThe room4 is a living room and you need the key from the Room1 to unlock the room3""")
corridor = Room("""This is Corridor.\nCorridor is where the front door is, get all the items and try to unlock the front door. YOu may need 3 items which is hammer, chain saw and driver. """)
prison = Room("""This is prison.\nThe prison is where we can get the hammer.  """)
master_room = Room("""This is master room.\nmaster room is look alright and you can get the driver.""")
room1.name = "room1"
room2.name = "room2"
room3.name = "room3"
room4.name = "room4"
kitchen.name = "kitchen"
corridor.name = "corridor"
prison.name = "prison"
master_room.name = "master_room"
# Room travel definition
# room 1
room1.east = room2
# room 2
room2.north = corridor
room2.south = kitchen
room2.east = room3
# room 3
room3.west = room2
# kitchen
kitchen.east = master_room
kitchen.north = room2
# corridor
corridor.south = room2
corridor.east = room4
# room4
room4.west = corridor
room4.east = prison
#prison
prison.west = room4
prison.south = master_room
#master
master_room.north = prison

# items definition
MAX_ITEM_USE_CNT = 5

Item.description = ""

key1 = Item("Shiny silver key", "silver key", "key")
key1.description = "You use it to escape the first room and to unlock the secret room."
key1.cnt = 0

key2 = Item("Rust key", "rust key", "key2")
key2.description = "You use it to unlock the prison"
key2.cnt = 0

driver = Item("driver")
driver.description = "The driver is to help you to unlock the front door. "
driver.cnt = 0

hammer = Item("hammer")
hammer.description = "The hammer is to unlock the front door."
hammer.cnt = 0

chain_saw = Item("chain saw")
chain_saw.description = "it is for unlock the front door."
chain_saw.cnt = 0

flare_gun = Item("flare gun")
flare_gun.description= "You have to shoot the flare gun for help after you escape the house."
flare_gun.cnt = 0

# Available items in each room
room1.items = Bag()
room2.items = Bag()
room3.items = Bag()
room4.items = Bag()
kitchen.items = Bag()
master_room.items = Bag()
prison.items = Bag()

room1.items.add(key1)
room2.items.add(chain_saw)
kitchen.items.add(key2)
master_room.items.add(driver)
prison.items.add(hammer)
room4.items.add(flare_gun)


#if current_room = room2 and item = key1

# Start from room1
current_room = room1
inventory = Bag()

# key1_used = False
# key2_used = False




front_door = 100

@when("exit")
def terminate():
    print("Terminate Adventure Game!!\nBye~~ See you again!")
    exit()

@when("use ITEM")
def escape(item):
    global front_door
    # Attack is only valid in corridor
    if current_room.name is not "corridor":
        print("You are in %s"%current_room.name)
        print("Move to corridor!!")
        return
        
    
    # if you have items in inventory
    if item in inventory:
        # only support driver, hammer, chain_saw and flare_gun
        if (item == "driver") or (item == "hammer") or (item == "chain saw") or (item == "flare gun"):
            escapeitem = inventory.take(item)
            escapeitem.cnt -= 1
            inventory.add(escapeitem)
            
            front_door -= 10
            print("Success Attack to front door by %s!!\nRemaining Power level: %d "%(escapeitem, front_door))
            
            if (front_door == 0):
                print("\nGAME OVER")
                print("You are FREE")
                print("You have escaped the island!\n")
                exit()
        else:
            print(f"{item} is not supported items")
    else:
        print(f"You do not have the {item}")
    


# @when("use flare gun")
# @when("use the flare gun")
# def escape():
#     if front_door == 0:
#         print("GAME OVER")
#         print("You have escaped the island!")
#     else:
#         print("You can't use flare gun")


@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
    if item in current_room.items:
        t = current_room.items.take(item)
        t.cnt = MAX_ITEM_USE_CNT
        inventory.add(t)
        print(t.cnt)
        print(f"You pick up the {item} with %s power"%str(t.cnt))
    else:
        print(f"you don't see a {item}")

@when ("go DIRECTION")
def travel(direction):
    global current_room
    dest_room = current_room.exit(direction)
    if dest_room: # if valid travel
        # Traveling from room1 to room2
        if current_room.name == "room1" and dest_room.name == "room2":
            print("You need silver key")
            item = "silver key"
            if item not in inventory:
                print("You need silver key in room1")
                return
        # Traveling from corridor to room4
        elif current_room.name == "corridor" and dest_room.name == "room4":
            print("You need silver key")
            item = "silver key"
            if item not in inventory:
                print("You need silver key in room1")
                return
        # Traveling from room4 to prison
        elif current_room.name == "room4" and dest_room.name == "prison":
            print("You need rust key")
            item = "rust key"
            if item not in inventory:
                print("You need rust key in kitchen")
                return
            # Harzard object is not allowed in prison
            item = "chain saw"
            if item in inventory:
                print("You can bring Weapon(chain saw) to prison")
                print("Drop your chain saw")
                return
        
        print('You go %s.' % direction)
        print("Traveling from %s to %s"%(current_room.name, dest_room.name))
        current_room = dest_room
        look()
    else:
        print("Invalid path - Not supported")

@when("look at ITEM")
@when("my ITEM")
def look_at(item):
    if item in inventory:
        t = inventory.find(item)
        print(t)
        print(t.description)
    else:
        print(f"you aren't carrying an {item}")

@when("inventory")
@when("show inventory")
@when("what is in my pocket")
def player_inventory():
    print("You are carrying")
    for item in inventory:
        print("%s with Power level: %d"%(item, item.cnt))
        

@when("drop ITEM")
def drop(item):
    obj = inventory.take(item)
    if not obj:
        print("You do not have a %s." % item)
    else:
        print("You drop the %s." % obj)
        current_room.items.add(obj)
        
# Display Current Room and available items
@when('look')
def look():
    say(current_room)
    if current_room.items:
        for i in current_room.items:
            say('A %s is here.' % i)


def main():
    print(current_room)
    start()

if __name__ == '__main__':
    main()