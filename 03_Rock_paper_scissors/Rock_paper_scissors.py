import random

def get_user_choice():
    print("\nChoose your move:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")

    choice = input("Enter 1, 2, or 3: ")
    choices = {"1": "rock", "2": "paper", "3": "scissors"}

    return choices.get(choice, None)


def get_computer_choice():
    choices = ["rock", "paper", "scissors"]
    return random.choice(choices)


def decide_winner(user, computer):
    if user == computer:
        return "It's a tie!"
    elif (user == "rock" and computer == "scissors") or \
         (user == "paper" and computer == "rock") or \
         (user == "scissors" and computer == "paper"):
        return "You win!"
    else:
        return "You lose! Computer wins."


def play_game():
    print("Welcome to Rock, Paper, Scissors!")

    while True:
        user_choice = get_user_choice()
        if not user_choice:
            print("Invalid choice. Please enter 1, 2, or 3.")
            continue

        computer_choice = get_computer_choice()
        print(f"\nYou chose: {user_choice.capitalize()}")
        print(f"Computer chose: {computer_choice.capitalize()}")

        result = decide_winner(user_choice, computer_choice)
        print(result)

        play_again = input("\nDo you want to play again? (y/n): ").lower()
        if play_again != "y":
            print("Thanks for playing! Goodbye!")
            break


if __name__ == "__main__":
    play_game()
