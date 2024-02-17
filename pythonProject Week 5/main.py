import random
print("Hello, welcome to a game of Hangman")
print("You only have 12 guesses")
#This is the secret word
secret_word="california"
letters_guessed=""
#Player only has a number of 12 guesses
incorrect_guesses= 12
#This is a loop where it will break once the player has made too many failed attempts
while incorrect_guesses <= 12:
    user_guess=input("Enter a letter:  ")
    if user_guess in secret_word:
        print(f"Correct! There is one or more {user_guess} in the secret word.")
    else:
        incorrect_guesses -= 1
        print(f"Incorrect. There are no {user_guess} in the secret word.{incorrect_guesses} turns left.")

    #Maintain a list of all letters guessed
    letters_guessed = letters_guessed + user_guess
    wrongLetterCount = 0

    for letter in secret_word:
        if letter in letters_guessed:
            print(f"{letter}", end="")
        else:
            print("_", end="")
            wrongLetterCount += 1

    if wrongLetterCount == 0:
        print(f"Congraulations! The secret word was: {secret_word}. You won!")
        break

else:
    print("Sorry, you didnt win this time. Try again")













