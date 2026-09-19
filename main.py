"Project 1 rock paper Sesior Game"

print("Rock Papper Sesior Game")

you = input("Enter yur choice: ")

import random

choices = ["rock", "paper", "scissor"]

computer = random.choice(choices)

print("You:", you)
print("Computer:", computer)

if you == "rock" and computer == "paper":
    print("Computer win 💻")

elif you == "rock" and computer == "scissor":
    print("You win 🏆")

elif you == "paper" and computer == "rock":
    print("You win 🏆")

elif you == "paper" and computer == "scissor":
    print("Computer win 💻")

elif you == "scissor" and computer == "rock":
    print("Computer win 💻")

elif you == "scissor" and computer == "paper":
    print("You win 🏆")

elif you == "rock" and computer == "paper":
    print("Computer win 💻")

elif you == "rock" and computer == "scissor":
    print("You win 🏆")

elif you == "paper" and computer == "rock":
    print("You win 🏆")

elif you == "paper" and computer == "scissor":
    print("Computer win 💻")

elif you == "scissor" and computer == "rock":
    print("Computer win 💻")

elif you == "scissor" and computer == "paper":
    print("You win 🏆")

elif you == computer:
    print("Draw ♻")

else:
    print("Invalid choice")