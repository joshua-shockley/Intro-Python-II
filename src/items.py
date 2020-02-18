
# create my Items class
import time


class Items:

    def __init__(self, name, description):
        self.name = name
        self.description = description

    def on_take(self):
        return f' picked up {self.name}'

    def on_drop(self):
        # return f'dropped {self.name}'
        if self.name == "lamp":
            print(f"OH!... Dang")
            time.sleep(1)
            print(
                f"your surrounding area got so dark that you could barely see you own feet on the floor below")
            time.sleep(2)
            print(f"maybe picking the lamp would be a good idea...")
        return f'dropped {self.name}'
