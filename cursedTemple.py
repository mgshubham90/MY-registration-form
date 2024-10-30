import random

# Game variables
player_health = 100
player_location = "entrance"
inventory = []

# Temple layout
temple_layout = {
    "entrance": {"north": "hallway", "description": "You stand in front of the ancient temple."},
    "hallway": {"north": "chamber", "south": "entrance", "description": "A long, dark hallway stretches before you."},
    "chamber": {"north": "treasure_chamber", "south": "hallway", "description": "A grand chamber with a high ceiling."},
    "treasure_chamber": {"south": "chamber", "description": "You've reached the treasure chamber! Congratulations!"},
    "trap_room": {"south": "hallway", "description": "You've triggered a deadly trap!"},
    "dragon_lair": {"south": "chamber", "description": "You've encountered a fierce dragon!"},
}

# Game functions
def go(direction):
    global player_location
    if direction in temple_layout[player_location]:
        player_location = temple_layout[player_location][direction]
        print(temple_layout[player_location]["description"])
    else:
        print("You can't go that way!")

def take(item):
    global inventory
    if item in ["key", "sword", "shield"]:
        inventory.append(item)
        print(f"You've taken the {item}!")
    else:
        print("You can't take that!")

def fight(creature):
    global player_health
    if creature == "dragon":
        if "sword" in inventory:
            print("You've defeated the dragon!")
            player_health += 20
        else:
            print("You're no match for the dragon! You lose 20 health.")
            player_health -= 20
    else:
        print("You can't fight that!")

def check_inventory():
    print("You have:")
    for item in inventory:
        print(item)

def play_game():
    while True:
        command = input("> ").split()
        if command[0] == "go":
            go(command[1])
        elif command[0] == "take":
            take(command[1])
        elif command[0] == "fight":
            fight(command[1])
        elif command[0] == "inventory":
            check_inventory()
        elif command[0] == "quit":
            print("Thanks for playing!")
            break
        else:
            print("Invalid command. Try again!")

play_game()
