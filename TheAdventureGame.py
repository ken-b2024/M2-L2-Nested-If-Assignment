#Task 1
place = input("Choose a place (forest/cave): ")

if place == "forest":
    action = input("Climb a tree or cross a river?: ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action != "climb a tree":
        print("You found a boat!")
else:
    print("You find a hidden treasure!")

#Task 2
place = input("Choose a place (forest/cave): ")

if place == "forest":
    action = input("Climb a tree or cross a river?: ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action != "climb a tree":
        print("You found a boat!")
if place == "cave":
    action = input("light a torch or proceed in the dark?: ")
    if action == "light a torch":
        print("You found a sleeping dragon guarding the hidden treasure!")
    elif action == "proceed in the dark":
        print("Uh-oh! You just stepped on the tail of a sleeping dragon!")

#Task 3
place = input("Choose a place (forest/cave): ")

if place == "forest":
    action = input("Climb a tree or cross a river?: ")
    if action == "climb a tree":
        print("You found a bird's nest!")
    elif action != "climb a tree":
        print("You found a boat!")
elif place == "cave":
    action = input("light a torch or proceed in the dark?: ")
    if action == "light a torch":
        print("You found a sleeping dragon guarding the hidden treasure!")
    elif action == "proceed in the dark":
        print("Uh-oh! You just stepped on the tail of a sleeping dragon!")
else:
    pass