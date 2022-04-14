'''
Escaping room adventure game

Authur : Eric Kim
         Y11, Kings High School
         
Date : 12/04/2022
Version : 0.4

<Romm map and items>
                                                         No Hazard 
                 flare gun           rust key           weapon allowed
       front door<------ corridor  <----------> room4  <---------->  prison
        (Exit)               ^               (flare gun)            (hammer) 
                             |                                         
                             |                                         
                             |                                         
             silver key      v                                         
   Room1    <-------->    Room2    <---------> Room3                   
(silver Key)           (Chain Saw)                                     
                            ^                                          
                            |                                          
                            |                                          
                            |                                          
                            v                                          
                         Kitchen   <------------------------------> master room
                        (Rust key)                                   (driver)


Note:
1. Player should find all the items in rooms to escape island
2. Exit, front door is located in corridor.
3. Player should utilize multiple items to break front door
4. Power level of front door is 100
5. Attack by each item could reduce the front door's power level by 10
6. Each item has 5 attack counter and it's reduced by 1 on each attack.
7. In order to recharge the attack counter, drop the item and pick up the item again.
8. Player can terminate the game in any room by "exit" command

'''                      
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

# No path between master room and prison


# items definition
MAX_ITEM_USE_CNT = 5
MAX_FRONT_DOOR_POWER_LEVEL = 100


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


# Start from room1
current_room = room1
inventory = Bag()

# Set power level of front door
front_door = MAX_FRONT_DOOR_POWER_LEVEL

# exit game
@when("exit")
def terminate():
    print("Terminate Adventure Game!!\nBye~~ See you again!")
    exit()

# Control escape room
# Attack front door by various items
# Default power level of front door: 100
# Each attack reduces 
#    the front door's power level by 10
#    the items remaining power by 1
@when("use ITEM")
def escape(item):
    global front_door
    # Attack is only valid in corridor
    if current_room.name is not "corridor":
        print("You are in %s"%current_room.name)
        print("Move to corridor!!")
        return
        
    if item == "flare gun":
        if front_door == 0:
            print("\nGAME OVER")
            print("You are FREE")
            print("You have escaped the island!\n")
            exit()
        else:
            print("You can't use flare gun")
            print("Front door is NOT broken yet. Need more attack.\n")
            return
    
    # if you have the items in your inventory
    if item in inventory:
        # only support driver, hammer, chain_saw and flare_gun
        if (item == "driver") or (item == "hammer") or (item == "chain saw") or (item == "flare gun"):
            
            # Update power level of items( reduce 1 power level on each use command)
            # Take item from inventory--> reduce power level by 1 --> Add the item to inventory again
            escapeitem = inventory.take(item)
            if( escapeitem.cnt != 0):
                escapeitem.cnt -= 1
                inventory.add(escapeitem)
                
                # reduce front door's remaining power level.
                if front_door >= 10:
                    front_door -= 10
                else:
                    front_door = 0 # Power level is Zero. Broken
                    
                print("Success Attack to front door by %s!!\nRemaining Power level: %d \n"%(escapeitem, front_door))
                print(f"{item} has %d power remaining"%escapeitem.cnt)
                
                # if front door power level is ZERO, let the player know that it's time to use flare gun.
                if (front_door == 0):
                    print("Front door is broken. It't time to use Flare gun to exit!!\n")
            else:
                # All Power is consumed. Need to be recharged the power of the item. 
                # Drop it and Get it again.
                print(f"No more power remaining in {item} !!\n")
                print(f"In order to charge the power, drop it and pick up the {item} again\n")
                
                # Now, this item has zero(0) power level
                inventory.add(escapeitem)
        else:
            # if not supported items are used( example: key )
            print(f"{item} is not supported item")
    else:
        # If you use an item that is not in your inventory.
        print(f"You do not have the {item}")

# Pick up item from current room
# Item power is reset to MAX upon getting item
@when("get ITEM")
@when("take ITEM")
@when("pick up ITEM")
def pickup(item):
    if item in current_room.items:
        t = current_room.items.take(item)
        # Assign default power level to the item. 5
        t.cnt = MAX_ITEM_USE_CNT 
        inventory.add(t)
        print(t.cnt)
        print(f"You pick up the {item} with %s power"%str(t.cnt))
    else:
        print(f"you don't see a {item}")

#
# Transition control.
# Check Key if required.
@when ("go DIRECTION")
def travel(direction):
    global current_room
    dest_room = current_room.exit(direction)
    if dest_room: # if valid travel
        # Traveling from room1 to room2
        if current_room.name == "room1" and dest_room.name == "room2":
            item = "silver key"
            if item not in inventory:
                print("You need silver key in room1")
                return
            else:
                print("You Opened the door with your silver key")
                
        # Traveling from corridor to room4
        elif current_room.name == "corridor" and dest_room.name == "room4":
            item = "silver key"
            if item not in inventory:
                print("You need silver key in room1")
                return
            else:
                print("You Opened the door with your silver key")
                
        # Traveling from room4 to prison
        elif current_room.name == "room4" and dest_room.name == "prison":
            item = "rust key"
            if item not in inventory:
                print("You need rust key in kitchen")
                return
            else:
                print("You opened the door with your rust key")
                
            # Harzard object is not allowed in prison
            item = "chain saw"
            if item in inventory:
                print("You can NOT bring Hazard material(chain saw) to prison")
                print("Drop your chain saw. You can pick up the chain saw later")
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
        
# Drop the item to current room
@when("drop ITEM")
def drop(item):
    # Remove item from inventory
    removeditem = inventory.take(item)
    if not removeditem:
        print("You do not have a %s." % item)
    else:
        print("You drop the %s." % removeditem)
        # Add the removed item to current room
        current_room.items.add(removeditem)
        
# Display Current Room and available items
@when('look')
def look():
    print(current_room)
    if current_room.items:
        print("\nAvailable items in this room :")
        for i in current_room.items:
            print('\tA %s is here.' % i)
    else:
        print("No more items available!")
        

def main():
    print(current_room)
    start()

if __name__ == '__main__':
    main()