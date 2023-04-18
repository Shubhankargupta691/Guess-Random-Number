# Guess-Random-Number

Python program that generates a random number between 1 and 100 and prompts the user to guess the number

Here's how the program works:

    We import the random module, which we'll use to generate a random number.
    We use the randint() function of the random module to generate a random number between 1 and 100, inclusive, and store it in the variable number.
    We use a while loop to repeatedly prompt the user to guess the number until they guess correctly.
    Inside the loop, we use the input() function to prompt the user to enter their guess. We convert the user's input to an integer using the int() function and store it in the variable guess.
    We check if the user's guess is equal to the random number. If it is, we print a congratulatory message and exit the loop using the break statement.
    If the user's guess is not equal to the random number, we provide feedback to the user by printing either "Too low. Guess again." or "Too high. Guess again." depending on whether the guess is lower or higher than the random number.
