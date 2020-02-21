

class Items:
    def __init__(self, name, description):
        self.name = name
        self.description = description

    def __str__(self):
        # want it to say its name then describe it
        return f"{self.name}, {self.description}"
