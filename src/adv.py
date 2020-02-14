from room import Room
from player import Player
# Declare all the rooms

room = {
    'outside': Room("Outside Cave Entrance", "North of you, the cave mount beckons", ["Broken Sword", "Rocks"]),

    'foyer': Room("Foyer", """Dim light filters in from the south. Dusty passages run north and east.""", ["Silver Coins", "Wand", "Torn Clothing"]),

    'overlook': Room("Grand Overlook", """A steep cliff appears before you, falling into the darkness. Ahead to the north, a light flickers in the distance, but there is no way across the chasm.""", ["Dragon Bones", "Broken Helm"]),

    'narrow': Room("Narrow Passage", """The narrow passage bends here from west to north. The smell of gold permeates the air.""", ["Gold Coins"]),

    'treasure': Room("Treasure Chamber", """You've found the long-lost treasure chamber! Sadly, it has already been completely emptied by earlier adventurers. The only exit is to the south."""),
}


# Link rooms together

room['outside'].n = room['foyer']
room['foyer'].s = room['outside']
room['foyer'].n = room['overlook']
room['foyer'].e = room['narrow']
room['overlook'].s = room['foyer']
room['narrow'].w = room['foyer']
room['narrow'].n = room['treasure']
room['treasure'].s = room['narrow']

# ? should room linked rooms be a dictionary instead?

p1 = Player(input("What is your name? \n"), room['outside'])

choice = 0
directions = ('w', 's', 'n', 'e')
while True:
    print(
        f"\nCurrent Location: {p1.current_room.name}\n{p1.current_room.desc}")
    choice = input(
        """
        What would you like to do?
        Go North[n], East[e], South[s], or West[w].
        Check inventory[i].
        Search area for items[r].
        Quit[q]
        """).lower().strip()
    # If the user enters a cardinal direction, attempt to move to the room there.
    if choice in directions:
        p1.move(choice)
    elif choice == "i":
        p1.print_items()
    elif choice == 'r':
        p1.current_room.print_items()
        # if len(p1.current_room.items) > 0:
        # inv_choice = input()

    elif choice == "q":
        print("You'll coward.")
        exit()
    else:
        print("Command not recognized! Enter a valid command.")
