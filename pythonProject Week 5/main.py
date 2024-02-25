#Week of 2/25/2024
#Chris Cooper
#Hangman Project
import random
print("Hello, welcome to a game of Hangman")
print("---------------------------------------------")
#Word dictionary that includes 4 words, these words are jumbled up
wordLibrary = ["texas","michigan","ohio","idaho"]
randomWord = random.choice(wordLibrary)
#This is the secret word
for x in randomWord:
    print("_", end="  ")
#Function that creates the hangman.
def print_gallows(wrong):
    if(wrong == 0):
        print("\n+---+")
        print("     |")
        print("     |")
        print("     |")
        print("    ===")
    elif(wrong == 1):
        print("\n+---+")
        print("O    |")
        print("     |")
        print("     |")
        print("    ===")
    if (wrong == 2):
        print("\n+---+")
        print("O     |")
        print("|     |")
        print("     |")
        print("    ===")
    if (wrong == 3):
        print("\n+---+")
        print(" O    |")
        print("/|    |")
        print("     |")
        print("    ===")
    if (wrong == 4):
        print("\n+---+")
        print(" O   |")
        print("/|\  |")
        print("     |")
        print("    ===")
    if (wrong == 5):
        print("\n+---+")
        print(" O    |")
        print("/|\   |")
        print("/     |")
        print("    ===")
    if (wrong == 6):
        print("\n+---+")
        print(" O    |")
        print("/|\    |")
        print("/ \    |")
        print("    ===")
#Created a print_hidden_word function that accepts arguments
def print_hidden_word(guessedLetters):
    counter=0
    rightLetters=0
    for char in randomWord:
        if(char in guessedLetters):
            print(randomWord[counter], end="  ")
            rightLetters+=1
        else:
            print("  ", end="  ")
        counter+=1
    return rightLetters
def printLines():
    print("\r")
    for char in randomWord:
        print("\u203E", end="  ")

length_of_word_to_guess = len(randomWord)
amount_of_times_wrong = 0
current_guess_index = 0
current_letters_guessed = []
current_letters_right = 0
#This is the loop for all the functions above
#Created a loop/function that asks user for input (ask_user_for_guess)
while(amount_of_times_wrong != 6 and current_letters_right != length_of_word_to_guess):
    print("\nLetters guessed so far: ")
    for letter in current_letters_guessed:
        print(letter, end="  ")
    ask_user_for_guess = input("\nGuess a letter: ")
    if(randomWord[current_guess_index] == ask_user_for_guess):
        print_gallows(amount_of_times_wrong)
    current_guess_index+=1
    current_letters_guessed.append(ask_user_for_guess)
    current_letters_right = print_hidden_word(current_letters_guessed)
    printLines()
else:
    amount_of_times_wrong+=1
    current_letters_guessed.append(ask_user_for_guess)
    print_gallows(amount_of_times_wrong)
    current_letters_right = print_hidden_word(current_letters_guessed)
    printLines()
#At the end, once all right letters, game is over is shown.
print("Game is over")
#Ignore SyntaxWarning lines, for some reason when making hangman arms/legs in brackets doesnt work in this version of python



