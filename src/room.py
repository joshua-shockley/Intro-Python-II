# Implement a class to hold room information. This should have name and
# description attributes.
import time


class Room:
    def __init__(self, name, description, items={}):
        self.name = name
        self.description = description
        # use the links to make attr
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        # for later when making items
        self.items = items

    def __str__(self):
        p_string = f"\n\n"
        time.sleep(1)
        p_string += f"\n{self.name}\n"
        p_string += f"\n{self.description}\n\n"
        p_string += f"\n{self.routes_str()} "
        return p_string


# next function matches up with the linked room on adv.py and the above {direction}_to  which sets up which direction has a next value or None as its set to None as default until it hits the linked rooms


    def get_room(self, direction):
        # this part is looking at whether there is an assignment of the .{direction}_to from above then created in the linked list in adv.py
        if hasattr(self, f"{direction}_to"):
            # this then returns the new assignment created by the link
            return getattr(self, f"{direction}_to")
        else:
            return None  # if no assignment then it changes nothing and player hasn't moved

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
        return f"\n possible routes are: {', '.join(self.get_routes())}\n"

    def get_room_items(self):
        if len(self.items) > 0:
            list = []
            time.sleep(1)
            print(f"you found:")
            for item in self.items:
                list.append(item)
                for thing in list:
                    # print(thing)
                    return thing
        else:
            return f"you found this area empty...\n\n nothing to collect!... "
