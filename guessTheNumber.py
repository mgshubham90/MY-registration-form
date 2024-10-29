import random

def guess_the_number():
    print("Welcome to 'Guess the Number' Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 10  # Maximum attempts allowed

    for attempt in range(1, attempts + 1):
        # Get user input
        try:
            guess = int(input(f"Attempt {attempt}/{attempts}: Take a guess: "))
        except ValueError:
            print("Please enter a valid number.")
            continue

        # Check if the guess is correct
        if guess < number_to_guess:
            print("Too low!")
        elif guess > number_to_guess:
            print("Too high!")
        else:
            print(f"Congratulations! You guessed the number in {attempt} attempts.")
            break
    else:
        # If the player didn't guess the number in the allowed attempts
        print(f"Sorry, you've run out of attempts. The number was {number_to_guess}.")

# Run the game
guess_the_number()
