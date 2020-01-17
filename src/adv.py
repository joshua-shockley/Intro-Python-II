from room import Room
from player import Player
from items import Items

# declare items
items = {
    'lamp': Items("Lamp", """looks old but still has fluid in it... you light it with the flint attatched to the bottom to get a better view"""),

    'cat': Items('Cat', """EEW! You can smell that cat from a mile away"""),

    'book': Items('Book', """You find this book on the floor near the window... it's in a language you're not familiar with"""),

    "binoculars": Items('Binoculars', """Brass viewing glasses that look older than yo' grandma's grandma... but somehow in mint condition"""),

    'chest': Items('Chest', """It's empty alright.... Dammit!""")
}


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", {"cat": items["cat"], "lamp": items["lamp"]}),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", {"book": items["book"], "binoculars": items["binoculars"]}),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", {"chest": items["chest"]}),
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


# def get_item():
#     collect = input(
#         "what do you want to do with 'all the things'...? ex: take item or drop item \n ---->  ")
#     split_up = collect.split()
#     if len(split_up) == 1 and split_up[0] == "neither":
#         print(f"ok.... then.... where to next {player.name}")
#         print(player.current_room.get_exits_string())  # prints exits
#         return 1
#     if len(split_up) == 2:
#         verb = str(split_up[0].lower())
#         noun = str(split_up[1].lower())
#         if noun in player.current_room.items:
#             if verb == "take":
#                 print(player.current_room.get_exits_string())
#                 player.add_item(noun)
#                 print(player.current_room.get_exits_string())
#             elif verb == "drop":
#                 print(
#                     f"{player.name}... you can't drop what you aren't holding.....")
#             else:
#                 print(
#                     'dont understand what you want to do here...\n take item, drop item or neither are the only acceptable answers')
#         elif noun in player.inventory.keys():
#             if verb == "drop":
#                 player.remove_item(noun)
#                 print(player.current_room.get_exits_string())
#             elif verb == "take":
#                 print(
#                     f"Really.... {player.name}... you are already carrying that.....")
#         elif noun == "inventory" or "stuff" or "things" or "items" or "i" and verb == "see":
#             print(player.inventory)

#         else:
#             print(f"how can you pick up {noun} if it's not here")


# Make a new player object that is currently in the 'outside' room.
# Write a loop that:

# * Prints the current room name
# * Prints the current description (the textwrap module might be useful here).

# * Waits for user input and decides what to do.


# If the user enters a cardinal direction, attempt to move to the room there.
# Print an error message if the movement isn't allowed.
#
# If the user enters "q", quit the game.
player = Player(input("pick a name for your player: "), room['outside'])
print(f'\n{player.name} is walking up to the cave and looks around..... \n {player.current_room.name} \n \n\n {player.current_room.description}')
directions = ("n", "s", "e", "w")
actions = ("take", "drop")
print(player.current_room.get_exits_string())
# now make the REPL
while True:

    # check for things in the room
    player.current_room.found_items(player.name)
    # make it so player can grab an item
    # make it so player can drop an item into the room list
    # ask for direction promt
    cmd = input("~~~~~> ").lower().split()
    if len(cmd) == 1:
        # check to see which direction
        if cmd[0] in directions:
            player.travel(cmd[0])
        elif cmd[0] == "q":
            print("Goodbye..... Quitter!")
            exit()
        elif cmd[0] == "help":
            print("help... until i make this more fun later")
        else:
            print("I don't get what you mean...either n,s,e,w or q for Quit")
    elif len(cmd) == 2:
        if cmd[0] == "take":
            player.add_item(cmd[1])
        elif cmd[0] == "drop":
            player.remove_item(cmd[1])
    else:
        print(f"\n{player.name} I don't know what you're doing but quit! \n")
