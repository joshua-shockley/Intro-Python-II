# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:

    def __init__(self, name, starting_room):
        self.name = name
        self.current_room = starting_room

        self.inventory = {}
    # sets current room and prints it... if unable to do the room movement it prints my move error

    def travel(self, direction):
        # player should be able to move in a direction
        next_room = self.current_room.get_room(direction)
        if next_room is not None:
            self.current_room = next_room
            print(self.current_room)
        else:
            print(
                f"{self.name} can't go that way... bruises or impeeding death await")

    def add_item(self, item):
        try:
            self.inventory[item] = self.current_room.items[item]
            del self.current_room.items[item]
            print(f'picked up {item}')
            self.has_what(self.inventory[item])
        except KeyError:
            print("wtf")

    def remove_item(self, item):
        try:
            self.current_room.items[item] = self.inventory[item]
            del self.inventory[item]
            self.droped_what(self.current_room.items[item])
        except KeyError:
            print('wtf')

    def has_what(self, item):
        print(f'{self.name} now has {item.on_take()}')

    def droped_what(self, item):
        print(f'{self.name} now has droped {item.on_take()}')
