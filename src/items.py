
# create my Items class


class Items:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        return f' picked up {self.name}'

    def on_drop(self):
        print(f'dropped {self.name}')
