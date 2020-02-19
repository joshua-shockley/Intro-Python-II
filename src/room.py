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
        p_string = f'\n this happens at the point of each init? \n'
        p_string += f"\n\n more stuff to print \n\n"
        p_string += f"\n{self.name}\n\n\n{self.description}\n\n"
        p_string += f"\n\n{self.routes_str()} "
        return p_string


# next function matches up with the linked room on adv.py and the above {direction}_to  which sets up which direction has a next value or None as its set to None as default until it hits the linked rooms

    def get_room(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        else:
            return None

# this method get the availabel routes from where current location is to the next
    def get_routes(self):
        exits = []
        if self.n_to:
            exits.append("n")
        if self.s_to:
            exits.append("s")
        if self.e_to:
            exits.append("e")
        if self.w_to:
            exits.append("w")
        return exits


# this method actually prints out the list of possible directions

    def routes_str(self):
        return f"\n\n possible routes are: {','.join(self.get_routes())}\n\n"
