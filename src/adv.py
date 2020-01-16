from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside':  Room("Outside Cave Entrance",
                     "North of you, the cave mount beckons"),

    'foyer':    Room("Foyer", """Dim light filters in from the south. Dusty
passages run north and east."""),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling
into the darkness. Ahead to the north, a light flickers in
the distance, but there is no way across the chasm."""),

    'narrow':   Room("Narrow Passage", """The narrow passage bends here from west
to north. The smell of gold permeates the air."""),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure
chamber! Sadly, it has already been completely emptied by
earlier adventurers. The only exit is to the south."""),
}


# come back later and see how to do this by accessing the dict room above
outside = Room("Outside cave Entrance", "North of you, the cave mount beckons")

foyer = Room(
    "Foyer", """Dim light filters in from the south. Dusty passages run north and east.""")

overlook = Room("Rand Overlook", """A seetp cliff appears before you, falling into the darkness. Ahead to the north, a light flicker in the distance, but there is no way across the chasm.""")

narrow = Room("Narrow Passage",
              """The narrow passage bends here from the west to north. the smell of gold permeates the air.""")

treasure = Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. the only exit is to the south.""")


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

# Make a new player object that is currently in the 'outside' room.
player_me = Player("Sir Turdly", "outside", [
                   "mp3 player", "gum", "pocket knife", "instructions"])
# Write a loop that:

while not next == 9:
    # * Prints the current room name
    now_in = player_me.in_room
    # * Prints the current description (the textwrap module might be useful here).

    if now_in == "outside":
        print(f'{player_me} is {outside.name}')
        print(outside.description)

    elif now_in == "foyer":
        print(f'{player_me} is in the {foyer.name}')
        print(foyer.description)

    elif now_in == "overlook":
        print(f'{player_me} is in the {overlook.name}')
        print(foyer.description)

    elif now_in == "narrow":
        print(f'{player_me} is in the {narrow.name}')
        print(narrow.description)

    elif now_in == "treasure":
        print(f'{player_me} is in the {treasure.name}')
        print(treasure.description)
    # * Waits for user input and decides what to do.
    #
    user_input = input("what do you want to do now? \n---->")

    next = user_input

    # If the user enters a cardinal direction, attempt to move to the room there.
    # Print an error message if the movement isn't allowed.
    #
    # If the user enters "q", quit the game.
    if next == "n":
        print("so you wanna go north")
        if now_in == "outside":
            player_me.in_room = "foyer"
        elif now_in == 'foyer':
            player_me.in_room = "overlook"
        elif now_in == "narrow":
            player_me.in_room = "treasure"
        else:
            print(f"{player_me} ran into the wall \n choose another direction")
    elif next == "s":
        print("so you wanna go south")
        if now_in == "foyer":
            player_me.in_room = "outside"
        elif now_in == "overlook":
            player_me.in_room = "foyer"
        elif now_in == "treasure":
            player_me.in_room = "narrow"
        else:
            print(f"{player_me} ran into the wall \n choose another direction")
    elif next == "w":
        print("so you wanna go west")
        if now_in == "narrow":
            player_me.in_room = "foyer"
        else:
            print(f'{player_me} ran into the wall \n choose another direction')
    elif next == "e":
        print("so you wanna go east")
        if now_in == "foyer":
            player_me.in_room = "narrow"
        else:
            print(f'{player_me} ran into the wall \n choose another direction')
    elif next == "q":
        print("okay try again next time...QUITER!")
        break
