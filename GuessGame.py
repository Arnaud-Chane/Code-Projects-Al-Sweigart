#GuessGame improved
import random

print("Hello ! What's your name ?")
myName = input("Hi ! I'm ")
print(f"Alright, then {myName}, let's play a game ! Guess a number between 0 and 10.")

number = random.randint(0, 10)
guessesTaken = 0
answer = 0

if answer == 0:
    for guessesTaken in range (5):
        print("Try to guess it.")
        guessNumber = input("")
        guessNumber = int(guessNumber)

        if guessNumber > number :
            print("Nope ! Too high. Try again.")
            guessesTaken += 1

        if guessNumber < number :
            print("It's too low. Try again !")
            guessesTaken += 1

        if guessNumber == number :
            guessesTaken += 1
            answer = 1
            break

if answer == 0:
        print("Try to guess it.")
        guessNumber = input("")
        guessNumber = int(guessNumber)

        if guessNumber > number :
            print("Nope ! Too high. Last try.")
            guessesTaken += 1

        if guessNumber < number :
            print("It's too low. Last try kid.")
            guessesTaken += 1

        if guessNumber == number :
            guessesTaken += 1
            answer = 1


if answer == 0:
        print("Try to guess it.")
        guessNumber = input("")
        guessNumber = int(guessNumber)

        if guessNumber > number :
            print("Nope ! Too high.")
            guessesTaken += 1

        if guessNumber < number :
            print("It's too low.")
            guessesTaken += 1

        if guessNumber == number :
            guessesTaken += 1
            answer = 1



if guessNumber == number :
    guessesTaken = str(guessesTaken)
    number = str(number)
    print(f"Hey ! You find the right number in {guessesTaken} attempts. The number was indeed the number {number}.")
    number = int(number)

if guessNumber != number :
    number = str(number)
    print(f"Too bad for you, the number was {number}.")