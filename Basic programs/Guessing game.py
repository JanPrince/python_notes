import random
try_again = True
while try_again == True:
    secret = random.randint(0, 100)

    print("Welcome to the ultimate guessing game")
    print("\n")
    print("Remember you've got only 10 chances")
    Guess = int(input("I have a number in mind bet 0 and 100, can you guess: "))

    for i in range(10):
        if i == 9:
            print("oops you've lost all lives")
            break
        if Guess == secret:
            print("Hurray you made it. \n score: ", 9 - i)
            break
        elif Guess < secret:
            print("wronggg you have", 9-i, "lives left")
            Guess = int(input("Please come up: "))
        elif Guess > secret:
            print("wronggg you have", 9 - i, "lives left")
            Guess = int(input("Please come down: "))
                       # this automatically breaks out of loop

    print('\n')

    User_again = int(input("Press 1 to start again"))
    if User_again == 1:
        try_again = True


