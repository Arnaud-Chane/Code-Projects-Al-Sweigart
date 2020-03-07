#Correction du livre
import random

guessesTaken = 0

print("Hello ! What's your name ?")
myName = input("Hi ! I'm ")
print(f"Alright, then {myName}, let's play a game ! Guess a number between 0 and 10.")

number = random.randint(0, 10)

for guessesTaken in range (6):
    print("Try to guess it.")
    guessNumber = input("")
    guessNumber = int(guessNumber)

    if guessNumber > number :
        print("Nope ! Too high. Try again.")

    if guessNumber < number :
        print("It's too low. Try again !")

    if guessNumber == number :
       break


if guessNumber == number :
    guessesTaken = str(guessesTaken + 1)
    number = str(number)
    print(f"Hey ! You find the right number in {guessesTaken} attempts. The number was indeed {number}.")
    number = int(number)


if guessNumber != number:
    number = str(number)
    print(f"Too bad, the number was {number}.")
