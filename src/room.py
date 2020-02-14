# Implement a class to hold room information. This should have name and
# description attributes.


class Room:
    """ """

    def __init__(self, name, desc, items=[]):
        self.name = name
        self.desc = desc
        self.items = items
        self.n = None
        self.s = None
        self.e = None
        self.w = None

    def __str__(self):
        return f"Name: {self.name}, {self.desc}, items: {self.items}"

    def print_items(self):
        if len(self.items) > 0:
            print("You see the following items in front of you:")
            for index, item in enumerate(self.items):
                print(f"Slot {index}: {item}")
        else:
            print("You don't notice anything of interest.")
