# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    def __init__(self, name, description, items={}):
        #name, description
        self.name = name
        self.description = description
        #n_to, s_to, e_to, w_to
        self.n_to = None
        self.s_to = None
        self.e_to = None
        self.w_to = None
        self.items = items

    def __str__(self):
        d_string = ""
        d_string = f"\n---------------------\n"
        d_string += f"\n{self.name}\n"
        d_string += f"\n {self.description}\n"
        d_string += f"\n{self.get_exits_string()}\n"

        return d_string

    def found_items(self, guy):
        if len(self.items) > 0:
            print('when looking around.....\n')
            for item in self.items:
                print(f' found this {item} ')
        else:
            return None

    def get_room(self, direction):
        if hasattr(self, f"{direction}_to"):
            return getattr(self, f"{direction}_to")
        else:
            return None

    def get_exits(self):
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

    def get_exits_string(self):
        return f"You can go: {','.join(self.get_exits())} "
