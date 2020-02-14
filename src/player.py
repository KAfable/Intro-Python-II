import functools
# Write a class to hold player information, e.g. what room they are in
# currently.


class Player:
    def __init__(self, name, initial_room):
        self.name = name
        self.current_room = initial_room
        self.inventory = []

    def move(self, direction):
        try:
            self.room = getattr(self.room, direction)
        except AttributeError:
            print("The room doesn't exist or movement isn't allowed.")

    def print_items(self):
        if len(self.inventory) > 0:
            print("You see the following items in front of you:")
            for item in self.inventory:
                print(item)
        else:
            print("You have nothing in your inventory.")

    def drop(self, ind):
        dropped = self.inventory.pop(ind)
        self.current_room.append(dropped)
        self.print_items()

    def grab(self, ind):
        grabbed = self.current_room.pop(ind)
        self.inventory.append(grabbed)
