import random
game_name = "GUESSING GENIUS"
#importing words from another file. The code produces a random word from the list which will be the word to guess.
words = []
with open("words.txt") as word_file:
    for line in word_file:
        words.append(line.rstrip().lower())

#creating empty lists for the three parameters the word can meet
misplaced_guesses = []
incorrect_guesses =[]
turns_allowed = 5
turns_taken= 0

#displaying the requirements and rules of the game
username = input("Enter your name:")
print(f"Welcome to GUESSING GENIUS, {username}!")
print(f"In this game, you are going to guess a word with 4 letters")
game_level = ["1","2","3"]
print("GAME LEVELS:\n 1. EASY \n  2. MEDIUM \n 3. HARD \n ")
print("\n")

while True:
    level_choice = input("Enter game level (1, 2, or 3): ").strip()
    if level_choice in game_level:
        break
    print("Invalid level choice. Please try again.")

#creating a loop to help user choose levels of difficulty
if level_choice == "1":
    word_to_guess = random.choice(words)
elif level_choice == "2":
    room = []
    with open("room.txt") as word_file:
        for line in word_file:
            room.append(line.rstrip().lower())
    word_to_guess = random.choice(room)   
elif level_choice == "3":
    word_to_guess = "lion"
    turns_allowed = 3

#checking each letter in the guess against the word to be guessed
while turns_taken<turns_allowed:
    print(f"You have {turns_allowed-turns_taken} turn(s) left. GOOD LUCK!")
    
    if level_choice == "1":
        print(words)
        guess = input("Please guess a word from this list of words:").lower()
        if len(guess) != 4 or not guess.isalpha():
            print("PLEASE ENTER A 4-LETTER WORD")    
            continue    
    elif level_choice == "2":
        print("Please answer the question with a 4-letter word:")
        guess = input("A 4-lettered item found in the bedroom:").lower() 
        if len(guess) != 4 or not guess.isalpha():
            print("PLEASE ENTER A 4-LETTER WORD")    
            continue
    elif level_choice == "3":
        guess = input("Please guess a four-letter word:").lower()        
        if len(guess) != 4 or not guess.isalpha():
            print("PLEASE ENTER A 4-LETTER WORD")    
            continue        
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

#modified game to use different letter length of words
#creating hard, medium, and easy levels for the game

#for the hard level, i will choose the word to guess, and the player will have three guesses
#for the medium level, ask a question that will be answered with the word to guess 

#for the easy level, the game will give the list of words the player is supposed to guess from
