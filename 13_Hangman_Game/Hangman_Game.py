word = "python"           
guessed = ""                
tries = 6                     

print("Welcome to Hangman!")

while tries > 0:
    wrong = 0

    # Show the word with _ for unguessed letters
    for ch in word:
        if ch in guessed:
            print(ch, end=" ")
        else:
            print("_", end=" ")
            wrong += 1

    print()

    # If no underscores → word is fully guessed
    if wrong == 0:
        print("You won! The word was:", word)
        break

    guess = input("Guess a letter: ")

    guessed += guess

    # Wrong guess case
    if guess not in word:
        tries -= 1
        print("Incorrect! Tries left:", tries)

        if tries == 0:
            print("Game Over! The word was:", word)
            break
