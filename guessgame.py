#Creating a Guess Game
import random
game_name = "WORD GUESS GENIUS"
word_bank=[]
with open("words.txt") as word_file:
    for line in word_file:
        word_bank.append(line.rstrip().lower())
word_to_guess = random.choice(word_bank)
misplaced_guesses = []
incorrect_guesses = []
turns_allowed = 5
turns_taken = 0

#Display Current Game State
print("Welcome to", game_name)
print("In this game, you will guess a word with", len(word_to_guess),"letters")
print("You have", turns_allowed-turns_taken, "turns left.", "GOOD LUCK!" )

while turns_taken < turns_allowed:
    # Get the player's guess
    guess = input("Guess a word: ").lower()

    # Check if the guess length equals 5 letters and is all alpha letters
    if len(guess) != len(word_to_guess) or not guess.isalpha():
        print("Please enter 5-letter word.")
        continue

    # Check each letter in the guess against the word's letters
    index = 0
    for c in guess:
        if c == word_to_guess[index]:
            print(c, end=" ")
            if c in misplaced_guesses:
                misplaced_guesses.remove(c)
        elif c in word_to_guess:
            if c not in misplaced_guesses:
                misplaced_guesses.append(c)
            print("_", end=" ")
        else:
            if c not in incorrect_guesses:
                incorrect_guesses.append(c)
            print("_", end=" ")
        index += 1

    print("\n")
    print("Misplaced letters: ", misplaced_guesses)
    print("Incorrect letters: ", incorrect_guesses)
    turns_taken += 1

    # Check if the player has won
    if guess == word_to_guess:
        print("Congratulations, you win!")
        break

    # Check if the player has lost
    if turns_taken == turns_allowed:
        print("Sorry, you lost. The word was", word_to_guess)
        break

    # Display the number of turns left and ask for another guess
    print("You have", turns_allowed- turns_taken, "turns left.")