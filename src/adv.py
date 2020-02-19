from room import Room
from player import Player
import time

# # declare items
# items = {
#     'lamp': Items("Lamp", """looks old but still has fluid in it... you light it with the flint attatched to the bottom to get a better view"""),

#     'cat': Items('Cat', """EEW! You can smell that cat from a mile away"""),

#     'book': Items('Book', """You find this book on the floor near the window... it's in a language you're not familiar with"""),

#     "binoculars": Items('Binoculars', """Brass viewing glasses that look older than yo' grandma's grandma... but somehow in mint condition"""),

#     'chest': Items('Chest', """It's empty alright.... Dammit!""")
# }


# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons", ),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east.""", ),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm.""", ),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south.""", ),
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
player = Player(input("pick a name for your player: "), room['outside'])
print(f'\n{player.name} is walking up to the cave and looks around..... \n \n{player.current_room.name} \n \n\n {player.current_room.description}\n\n')
directions = ("n", "s", "e", "w")
commands = ("n", "s", "e", "w", "q")

print(room['outside'])
