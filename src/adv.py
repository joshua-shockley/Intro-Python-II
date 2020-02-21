from room import Room
from item import Items
from player import Player
from help import help
from quit import *
import time

# declare items
items = {
    'lamp': Items("Lamp", """looks old but still has fluid in it... you light it with the flint attatched to the bottom to get a better view"""),

    'cat': Items('Cat', """EEW! You can smell that cat from a mile away"""),

    'book': Items('Book', """You find this book on the floor near the window... it's in a language you're not familiar with"""),

    "binoculars": Items('Binoculars', """Brass viewing glasses that look older than yo' grandma's grandma... but somehow in mint condition"""),

    'chest': Items('Chest', """It's empty alright.... Dammit!"""),

    'coins': Items("Coins", """What! you found some coins in the corner under the book.... take that shtuff!"""),
}


# Declare all the rooms
room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons",),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", {"Cat": items["cat"]}),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", {"binoculars": items["binoculars"]}),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air.""", []),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", {"book": items["book"], "chest": items["chest"], "coins": items["coins"]}),
}

# Link rooms together

room['outside'].n_to = room['foyer']
room['foyer'].s_to = room['outside']
room['foyer'].n_to = room['overlook']
room['foyer'].e_to = room['narrow']
room['overlook'].s_to = room['foyer']
room['narrow'].w_to = room['foyer']
room['narrow'].n_to = room['treasure']
room['treasure'].s_to = room['narrow']
#
# Main
#
# this sets up picking up or droping items
# Make a new player object that is currently in the 'outside' room.
# Write a loop that:
# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).
# * Waits for user input and decides what to do.
# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.

# making functions to call in the while loop

directions = ("n", "s", "e", "w")
player_gear_cmds = ('gear', 'stuff', 'items', 'i',
                    'describe', 'desc', 'd', 'take')
room_items_cmds = ("things", "items", "i", )
player = Player(input("pick a name for your player: "), room['outside'])

print(f'\n{player.name} is walking up to the cave and looks around..... \n')
time.sleep(2)
print(f'\n{player.current_room.name} \n ')
time.sleep(1.5)
print(f'\n\n {player.current_room.description}\n\n')
time.sleep(1.5)
print(player.current_room.routes_str())

while True:
    # check for things in the room
    print(player.current_room.get_room_items())
    cmd = input('-------> ').lower().split()
    print(cmd)
    if len(cmd) == 1:
        if cmd[0] in directions:
            player.moves(cmd)
            time.sleep(1)
        elif cmd[0] == "help":
            time.sleep(1)
            help(player.name)
            print(player.current_room.routes_str())
        elif cmd[0] == "q":
            quit(player.name)
    elif len(cmd) == 2:
        if cmd[0] == "player":
            if cmd[1] in player_gear_cmds:
                if cmd[1] == "gear" or cmd[1] == "stuff" or cmd[1] == "items" or cmd[1] == "i":
                    time.sleep(1)
                    player.gear()
                elif cmd[1] == "describe" or cmd[1] == "desc" or cmd[1] == "d":
                    time.sleep(1)
                    info = input(
                        "what is the item you want to look at?\n--->  ")
                    ## still need to re-reference how to pull up the class name and description separately ##
                    print(items.get(info))
            else:
                print(
                    f"you didnt enter a proper option\n\n try one of the following for the second entry, example: 'player' 'second entry'\n\n")
                for option in player_gear_cmds:
                    print(option)
        if cmd[0] == "take":
            print('take what?')
        if cmd[0] == 'drop':
            print('what did you drop now?')
        else:
            print("currently what you have typed isn't going to do anything")
            print(cmd)
