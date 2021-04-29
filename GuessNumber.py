# This is the guess the number game
import random

print('Hello. What is your name?')
name = input()

print('Well, ' +name+ ', I am thinking of a number between 1 and 20.')
secretNumber = random.randint(1,20)

for guessesTaken in range(1,7):
    print('Take a guess: ')
    guess = int(input())

    if guess > secretNumber:
        print('Your guess is too high')
    elif guess < secretNumber:
        print('Your guess is too low')
    else:
        break #This condition is for the correct guess!

if  guess == secretNumber:
    print('Good job, ' +name+ '! You guessed the number in ' + str(guessesTaken) + ' tries.')
else:
    print('Nope. The number is ' + str(secretNumber) + ' but thanks for trying!')
