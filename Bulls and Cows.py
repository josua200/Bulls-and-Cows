print("This game is called Bulls and Cows. The directions are simple,you have to guess the 4 digit number. if you reach 4 bulls, you win the game.")
import random
secret_number = ''.join(random.sample('0123456789', 4))
def get_bulls_and_cows(secret, guess):
    bulls = sum(1 for s, g in zip(secret, guess) if s == g)
    cows = sum(1 for g in guess if g in secret) - bulls
    return bulls, cows


attempts = 0
while True:
    guess = input("Enter your guess: ")
    attempts += 1

    if len(guess) != 4 or not guess.isdigit():
        print("Please enter a 4-digit number.")
        continue

    bulls, cows = get_bulls_and_cows(secret_number, guess)
    print(f"Bulls: {bulls}, Cows: {cows}")
    if bulls == 4:
        print(f"Congratulations! You guessed the number in {attempts} attempts.")
        break

