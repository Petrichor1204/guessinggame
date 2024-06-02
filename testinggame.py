import random
game_name = "GUESSING GENIUS"
#importing words from another file. The code produces a random word from the list which will be the word to guess.
words = []
with open("words.txt") as word_file:
    for line in word_file:
        words.append(line.rstrip().lower())
    print(words)
word_to_guess = random.choice(words)    

#creating empty lists for the three parameters the word can meet
misplaced_guesses = []
incorrect_guesses =[]
turns_allowed = 5
turns_taken= 0

#displaying the requirements and rules of the game
username = input("Enter your name:")
print("Welcome to GUESSING GENIUS", username, "!")
print("In this game, you are going to guess a word with", len(word_to_guess), "letters")
print("You have",turns_allowed-turns_taken, "turns left. GOOD LUCK!")

#creating a loop 
while turns_taken<turns_allowed:
    
    guess = input("Please enter a word:").lower()
    if len(guess) != len(word_to_guess) or not guess.isalpha():
        print("Please enter a 4-letter word:")
        continue
#checking each letter in the guess against the word to be guessed
    index = 0
    for c in guess:
        if c == word_to_guess[index]:
            print(c, end=" ")
            if c in misplaced_guesses:
                misplaced_guesses.remove(c)
        elif c in word_to_guess:
            if c not in misplaced_guesses:
                misplaced_guesses.append(c)
            print("_",end=" ")
        else:
            if c not in incorrect_guesses:
                incorrect_guesses.append(c)  
            print("_", end= " ")      
        index += 1
    print("\n")
    print("misplaced letters:", misplaced_guesses)
    print("incorrect letters:", incorrect_guesses)
    turns_taken +=1
    #checking if the player has won
    if guess == word_to_guess:
        print("Congratulations! You win!")
        break

#checking if the player has lost
    if turns_taken==turns_allowed:
        print("Sorry, You Lost, the word was: ", word_to_guess)
        break
#displaying number of turns left and asking for a guess
    print("You have", turns_allowed-turns_taken, "number of turns left")
#modified game to use different letter length of words
#creating hard, medium, and easy levels for the game

#for the medium level, there will be no list, and the player will have five guesses
#for the hard level, ask a question that will be answered with the word to guess and give ten tries

#for the easy level, the game will give the list of words the player is supposed to guess from, the player will have five guesses
