import sys
import random

secretNumber = random.randint(1,50)
print("I am thinking of a number between 1 and 50.\nYou have 5 chances to guess the number.")

print("Take a guess:")
guess = input()

if guess == 'exit':
    sys.exit()
    
guess = int(guess)

for guessTaken in range(1, 5):
    if guess < secretNumber:
        print("Your guess is too low.\n You have " + str(7 - guessTaken) + " guesses left.\nTake a guess again:")
        guess = int(input())
    elif guess > secretNumber:
        print("Your guess is too high.\n You have " + str(7 - guessTaken) + " guesses left.\nTake a guess again:")
        guess = int(input())
    else:
        break

if guess == secretNumber:
    print("Good job! You guessed my number in " + str(guessTaken) + " guesses!")
else:
    print("Nope! The number was " + str(secretNumber))
