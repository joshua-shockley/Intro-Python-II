
# create my Items class


class Items:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        return f' picked up {self.name}'

    def on_drop(self):
        return f'dropped {self.name}'


class LightSource(Items):
    def __init__(self, name, description):
        super().__init__(name, description)
        self.name = name
        self.description = description

    def on_drop(self):
        return f"dropped the {self.name}..\n It's not wise to drop you source of light"


class Treasure(Items):
    def __init__(self, name, description, special):
        super().__init__(name, description)
        self.name = name
        self.description = description
        self.special = special
