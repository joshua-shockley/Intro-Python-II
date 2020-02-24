# Write a class to hold player information, e.g. what room they are in
# currently.
import time


class Player:

    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room
        #self.description= description
        self.inventory = {}

    def __str__(self):
        return f"{self.name}"

    def take_talk(self):
        return f"take what?"

    def drop_talk(self):
        return f"what did you drop now?"

    # sets current room and prints it... if unable to do the room movement it prints my move error

    def moves(self, direction):
        next = self.current_room.get_room(direction)
        if next is not None:
            self.current_room = next
            print(self.current_room)
        else:
            print(f"{self.name}, You aren't able to go that way")
            time.sleep(2)
            print(f"bruises or impeeding death awaits if you keep that up")

    def gear(self):
        # list = []
        print(f"{self.name} has:")
        time.sleep(1)
        if len(self.inventory) > 0:
            for item in self.inventory:
                print(item)
                # list.append(item)
                # for thing in list:
                #     print(thing)
        else:
            print(f"Nothing, you got no Shtuff!")
