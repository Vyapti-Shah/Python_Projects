# rock, paper and scissors
import random

while True:
    choices = ["rock","paper","scissors"]

    computer = random.choice(choices)

    player = None
    while player not in choices:
        player = input("rock, paper or scissors? : ").lower()

    if player == computer:
        print("Computer : " + computer)
        print("Player : " + player)
        print("It's a TIE!")
    elif player == "rock":
        if computer == "paper":
            print("Computer : " + computer)
            print("Player : " + player)
            print("You LOSE!")
        if computer == "scissors":
            print("Computer : " + computer)
            print("Player : " + player)
            print("You WIN!")
    elif player == "scissors":
        if computer == "rock":
            print("Computer : " + computer)
            print("Player : " + player)
            print("You LOSE!")
        if computer == "paper":
            print("Computer : " + computer)
            print("Player : " + player)
            print("You WIN!")
    elif player == "paper":
        if computer == "scissors":
           print("Computer : " + computer)
           print("Player : " + player)
           print("You LOSE!")
        if computer == "rock":
           print("Computer : " + computer)
           print("Player : " + player)
           print("You WIN!")

    play_again = input("Play Again? (yes/no) : ").lower()
    if play_again != "yes":
        break
print("Bye!")