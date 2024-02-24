#Lab 6 - Chris Cooper
#Create a function that accepts a string and scrambles the string up.
import random
import math

#This is a word scrambler that I created.
scrambled_words="nigeria","italy","morocco"
word=random.choice(scrambled_words)
letters=list(scrambled_words)
random.shuffle(letters)
jumbled_word="".join(letters)
print("Your words are nigeria, italy, or morocco. Guess which one.")
#Just put in a word, how it works is it shuffles up the word and if you pick the right or wrong word it will break the function.
def word_scrambler():
    if input("Ok, make a guess\n")==word:
        print("Good job")
    else:
        print("Nope.Wrong")
word_scrambler()