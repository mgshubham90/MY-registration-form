import random

def word_wizard():
    words = ["python", "programming", "computer", "algorithm", "database", "network", "software", "developer", "interface", "variable"]
    max_attempts = 6
    
    print("Welcome to Word Wizard!")
    print("I'm thinking of a word. Can you guess it?")
    print(f"You have {max_attempts} incorrect guesses before the game ends.")
    
    word = random.choice(words)
    guessed_letters = set()
    correct_guesses = set()
    
    def display_word():
        return ''.join(letter if letter in correct_guesses else '_' for letter in word)
    
    while max_attempts > 0:
        print("\n" + display_word())
        print(f"Guessed letters: {' '.join(sorted(guessed_letters))}")
        print(f"Attempts left: {max_attempts}")
        
        guess = input("Guess a letter: ").lower()
        
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single letter.")
            continue
        
        if guess in guessed_letters:
            print("You already guessed that letter.")
            continue
        
        guessed_letters.add(guess)
        
        if guess in word:
            correct_guesses.add(guess)
            print("Correct guess!")
            
            if set(word) == correct_guesses:
                print(f"\nCongratulations! You've guessed the word: {word}")
                return
        else:
            max_attempts -= 1
            print("Incorrect guess.")
    
    print(f"\nGame over! The word was: {word}")

# Start the game
word_wizard()
