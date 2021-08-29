"""
 a game  -  guessing game but more advanced
"""
import random

lives = 9              # player's number of lives
words = ["piaza", "fairy", "teeth", "polar", "krsna",
         "plane", "outer", "shirt"]

secret_word =random.choice(words)               # random.choice(..) is used to select an element randomly from a list
clue = list("?????")      # list(..) is used for casting an object into list
heart_symbols = u'\u2764'           # symbols to represent the number of lives
guessed_word_correctly = False


#        Main code

def update_clue(guessed_letter,secret_word, clue):
    """
    input: takes in guessed_letter, secret word and clue
    if the guessed_letter is found in the secret_word, the clue is updates
    """
    index = 0
    while index < len(secret_word):
        if guessed_letter == secret_word[index]:
            clue[index] = guessed_letter
        index += 1


while lives > 0 :                   # loop keeps the game running if there are lives
    print(clue)
    print("lives left: " + heart_symbols * lives)
    guess = input("enter a word or the whole word : ")

    if guess == secret_word:
        guessed_word_correctly = True
        break


    if guess in secret_word:
        update_clue(guess, secret_word,clue)
    else:
        print("incorrect, you lose a life..")
        lives = lives - 1
    if clue == list(secret_word):
        guessed_word_correctly =True
        break


if guessed_word_correctly:
    print("you won, the secret word was " + secret_word)
else:
    print("you lost, the secret word was " + secret_word)