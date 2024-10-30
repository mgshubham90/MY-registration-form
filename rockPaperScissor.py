import random
import time

def rock_paper_scissors():
    choices = ["rock", "paper", "scissors"]
    player_score = 0
    computer_score = 0
    
    print("Welcome to Rock, Paper, Scissors!")
    print("First to win 3 rounds wins the game.")
    print("Type 'quit' to end the game.\n")

    while True:
        # Get player's choice
        player_choice = input("\nChoose rock, paper, or scissors: ").lower()
        
        # Check if player wants to quit
        if player_choice == 'quit':
            print("\nThanks for playing!")
            break
            
        # Validate input
        if player_choice not in choices:
            print("Invalid choice! Please choose rock, paper, or scissors.")
            continue

        # Computer makes a choice
        computer_choice = random.choice(choices)
        
        # Build suspense
        print("\nRock...")
        time.sleep(0.5)
        print("Paper...")
        time.sleep(0.5)
        print("Scissors...")
        time.sleep(0.5)
        
        # Show choices
        print(f"\nYou chose: {player_choice}")
        print(f"Computer chose: {computer_choice}")

        # Determine winner
        if player_choice == computer_choice:
            print("It's a tie!")
        elif (player_choice == "rock" and computer_choice == "scissors") or \
             (player_choice == "paper" and computer_choice == "rock") or \
             (player_choice == "scissors" and computer_choice == "paper"):
            print("You win this round!")
            player_score += 1
        else:
            print("Computer wins this round!")
            computer_score += 1

        # Show current score
        print(f"\nScore - You: {player_score} Computer: {computer_score}")

        # Check if someone has won the game
        if player_score == 3:
            print("\nCongratulations! You've won the game!")
            break
        elif computer_score == 3:
            print("\nGame Over! The computer wins!")
            break

# Start the game
rock_paper_scissors()
