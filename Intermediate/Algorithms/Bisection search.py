"""
Bisection search
problem: Guessing a secret number bet 0 and 100
"""
import random

secret_number = 9

low = 0
high =100
num_of_guess = 0

'''
for i in range(101):
    guess = (high + low) / 2
    num_of_guess += 1
    if guess > secret_number:
        high = guess
    elif guess < secret_number:
        low = guess
    else:
        break
print(guess)
print(num_of_guess, "guesses")
'''



guess = (high + low)/2           # first guess
for i in range(101):
    num_of_guess +=1
    if guess > secret_number:
        high = guess
    elif guess < secret_number:
        low = guess
    else:
        break
    guess = (high + low) / 2

print(guess)
print(num_of_guess, 'guesses')

