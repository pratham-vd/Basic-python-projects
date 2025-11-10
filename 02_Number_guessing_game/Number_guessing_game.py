import random

def number_guessing_game():
    print("Welcome to the Number Guessing Game!")
    print("I'm thinking of a number between 1 and 100.")
    
    # Generate a random number between 1 and 100
    number_to_guess = random.randint(1, 100)
    attempts = 0
    
    while True:
        try:
            # Take user input
            guess = int(input("Enter your guess: "))
            attempts += 1
            
            # Check the guess
            if guess < number_to_guess:
                print("Too low! Try again")
            elif guess > number_to_guess:
                print("Too high! Try again")
            else:
                print(f"Correct! The number was {number_to_guess}.")
                print(f"You guessed it in {attempts} attempts.")
                break
                
        except ValueError:
            print("Please enter a valid number.")

# Run the game
number_guessing_game()
