#GUESS THE NUMBER game
import random


def get_guess(number):
    guess = int(input("Please enter your guess: "))
    if guess == number:
        print("You guessed correctly!, You Win")

    elif guess < number:
        print("Your guess is too low")
        get_guess(number)

    elif guess > number:
        print("Your guess is too high")
        get_guess(number)


difficulty = input("Please enter the difficulty of the game (easy, medium, hard): ")
if difficulty == "easy":
    number = random.randint(0, 10)
    print("Guess the number between 0 - 10")
    get_guess(number)

elif difficulty == "medium":
    number = random.randint(0, 50)
    print("Guess the number between 0 - 50")
    get_guess(number)

elif difficulty == "hard":
    number = random.randint(0, 100)
    print("Guess the number between 0 - 100")
    get_guess(number)

else:
    print("Please enter a valid difficulty")
