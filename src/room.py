# Implement a class to hold room information. This should have name and
# description attributes.
import time


class Room:
    def __init__(self, name, description):
        self.name = name
        self.description = description
        # use the links to make attr
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        # for later when making items
        self.items = {}

    def __str__(self):
        print('\n this happens at the point of each init?')
        print("\n\n more stuff to print \n\n")
        return f"\n{self.name}\n\n\n{self.description}"
