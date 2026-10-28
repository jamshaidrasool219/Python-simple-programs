# Program: Rock Paper Scissors
import random

choices = ["rock", "paper", "scissors"]
user = input("rock, paper ya scissors: ").lower()
computer = random.choice(choices)

print("Computer ne chuna:", computer)

if user not in choices:
    print("Ghalat choice!")
elif user == computer:
    print("Barabar (Tie)!")
elif (user == "rock" and computer == "scissors") or \
     (user == "paper" and computer == "rock") or \
     (user == "scissors" and computer == "paper"):
    print("Aap jeet gaye!")
else:
    print("Computer jeet gaya!")
