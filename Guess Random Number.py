import random
number = random.randint(1,5)
for i in range(0,5):
    user = int(input("Guess the number"))
    if user  == number:
        print('hurray')
        print(f"your guesss number is right {number}")
        break
if user != number:
    print(f"your guesss number is incorrect {number}")