# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, in_room, inventory):
        self.name = name
        self.in_room = in_room
        self.inventory = inventory

    def __repr__(self):
        return self.name

    def taunt(self):
        print("let's tango!...Merica!")

    def greet(self):
        print("Hello!..Good day to you.")

    def goodbye(self):
        return "Screw this, I QUIT!"
