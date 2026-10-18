import random

def play_hangman():
    # 1. Setup words & game state
    words = ["python", "codealpha", "developer", "program", "hangman"]
    secret_word = random.choice(words).lower()
    
    guessed_letters = set()
    incorrect_guesses = 0
    max_incorrect = 6

    print("================================")
    print("      WELCOME TO HANGMAN        ")
    print("================================")
    print(f"Rule: You get {max_incorrect} incorrect guesses.\n")

    # 2. Main Game Loop
    while incorrect_guesses < max_incorrect:
        # Display current word state (e.g., p _ t h _ n)
        displayed_word = " ".join([letter if letter in guessed_letters else "_" for letter in secret_word])
        print(f"Word: {displayed_word}")
        print(f"Guessed letters: {sorted(list(guessed_letters))}")
        print(f"Incorrect guesses left: {max_incorrect - incorrect_guesses}")
        
        # Get user input
        guess = input("Guess a letter: ").lower()
        
        # Validation
        if len(guess) != 1 or not guess.isalpha():
            print("Please enter a single valid alphabet letter.\n")
            continue
            
        if guess in guessed_letters:
            print(f"You already guessed the letter '{guess}'. Try another one.\n")
            continue
            
        guessed_letters.add(guess)
        
        # Check if guess is correct
        if guess in secret_word:
            print(f"Good job! '{guess}' is in the word.\n")
        else:
            incorrect_guesses += 1
            print(f"Wrong guess! '{guess}' is not in the word.\n")
            
        # Check for win condition
        if all(letter in guessed_letters for letter in secret_word):
            print(f"Congratulations! You guessed the secret word: {secret_word}")
            break
    else:
        # Executed if the loop finishes without breaking (out of guesses)
        print("================================")
        print("         GAME OVER!             ")
        print(f"The secret word was: {secret_word}")
        print("================================")

if __name__ == "__main__":
    play_hangman()