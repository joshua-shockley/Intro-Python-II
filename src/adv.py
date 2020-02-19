from room import Room
from player import Player
from help import help
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

# making functions to call in the while loop


player = Player(input("pick a name for your player: "), room['outside'])


def quit(user):
    print('aaaaah... fine see you later')
    time.sleep(1)
    print(f'by {user}!')
    time.sleep(2)
    exit()


# def help():
#     print("tell me what you need help with here\n")
#     h_cmd = input(
#         f"{player.name}, what do you need help with?...\n\n examples: \n game play  all possible commands").lower()
#     if h_cmd is None:
#         print('you have to type something for me to know how to help...')
#         help()
#     elif h_cmd == "":
#         print('you have to type something for me to know how to help...')
#         help()
#     elif h_cmd == "life":
#         print('life is life dude.... just go live it!')
#     elif h_cmd == "love":
#         print("love hard and love fiercely. Otherwise what's the point")
#     elif h_cmd == "money":
#         print(
#             "I really don't know what to tell you about money.... \n\n I don't have any either. :(")
#     elif h_cmd == "fashion":
#         print("It's all bullshit really... But, there are some poorly designed styles out there, so really think it through.")
#     elif h_cmd == "game play":
#         print('follow the directions as you go. \nIt gets much easier if you read what the display asks for or shows as an option. \nMost commands are explained in the request. \n\n For a full list of the commands; after entering "help" enter "all possible commands". \nThis will show all commands whether for game play or help menu.')


print(f'\n{player.name} is walking up to the cave and looks around..... \n \n{player.current_room.name} \n \n\n {player.current_room.description}\n\n')
directions = ("n", "s", "e", "w")
print(player.current_room.routes_str())

while True:
    cmd = input('-------> ').lower()
    if cmd in directions:
        time.sleep(1)
        player.moves(cmd)
    elif cmd == "help":
        time.sleep(1)
        help(player.name)
        print(player.current_room.routes_str())
    elif cmd == "q":
        quit(player.name)
