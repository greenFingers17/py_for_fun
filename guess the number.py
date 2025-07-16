# This is a guess the number game

import random

print('Hi there! What is your name?')
playerName = input()

print('Well, ' + playerName + ', I am thinking between 1 and 20.')
secretNumber = random.randint(1, 20)

for guessesTaken in range(1, 7):
    print('Take a guess')
    guess = int(input())

    if guess < secretNumber:
        print('Your guess is too low.')
    elif guess > secretNumber:
        print('Your guess is too high.')
    else:
        break # This condition is for the correct guess!

if guess == secretNumber:
    print('Good job, ' + playerName + '! You guessed my number in ' + str(guessesTaken) + ' guesses!')   
else:
    print('Nope. The number I was thinking of was ' + str(secretNumber) + '.') 
    


