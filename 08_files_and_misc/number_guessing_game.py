# Program: Number guessing game
import random

secret = random.randint(1, 100)
attempts = 0

print("Maine 1 se 100 ke darmiyan ek number socha hai. Guess karein!")

while True:
    guess = int(input("Aap ka guess: "))
    attempts += 1

    if guess < secret:
        print("Aur bara number likhein")
    elif guess > secret:
        print("Aur chota number likhein")
    else:
        print(f"Shabash! {attempts} koshishon mein sahi guess kiya.")
        break
