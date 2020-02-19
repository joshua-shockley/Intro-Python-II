# Write a class to hold player information, e.g. what room they are in
# currently.
import time


class Player:

    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room

        # self.inventory = {}
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
