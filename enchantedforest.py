import random

def enchanted_forest():
    player_health = 100
    player_gold = 0
    inventory = []

    def print_status():
        print(f"\nHealth: {player_health} | Gold: {player_gold} | Inventory: {', '.join(inventory)}")

    def encounter_event():
        events = [
            ("You find a healing spring", "drink", 20, 0, None),
            ("You discover a gold nugget", "take", 0, 10, None),
            ("You see a mysterious potion", "drink", -10, 0, "potion"),
            ("A friendly elf offers you a magic ring", "accept", 0, 0, "magic ring"),
            ("You encounter a goblin", "fight", -15, 5, None),
            ("You find a treasure chest", "open", 0, 20, None),
            ("You see a sleeping dragon", "sneak", -5, 50, "dragon scale"),
            ("You discover an ancient sword", "take", 0, 0, "ancient sword"),
        ]
        return random.choice(events)

    print("Welcome to the Enchanted Forest!")
    print("Your goal is to survive and collect as much gold as possible.")
    print("Type 'quit' at any time to end the game.")

    while player_health > 0:
        print_status()
        event, action, health_change, gold_change, item = encounter_event()
        print(f"\n{event}!")
        choice = input(f"Do you want to {action}? (yes/no): ").lower()

        if choice == 'quit':
            break
        elif choice == 'yes':
            player_health += health_change
            player_gold += gold_change
            if item:
                inventory.append(item)
                print(f"You obtained: {item}")
            if health_change != 0:
                print(f"Your health changed by {health_change}")
            if gold_change != 0:
                print(f"You {'gained' if gold_change > 0 else 'lost'} {abs(gold_change)} gold")
        else:
            print("You decide to move on.")

        if player_health <= 0:
            print("\nGame Over! You have run out of health.")
            break

    print(f"\nFinal Status:")
    print_status()
    print("Thanks for playing The Enchanted Forest!")

# Start the game
enchanted_forest()
