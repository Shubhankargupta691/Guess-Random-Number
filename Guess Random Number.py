import random

number = random.randint(1, 100)
while True:
    guess = int(input("Guess the number"))
    if guess == number:
        print("Congratulations! You guessed the number.")
        break
    elif guess < number:
        print("Too low. Guess again.")
    else:
        print("Too high. Guess again.")
