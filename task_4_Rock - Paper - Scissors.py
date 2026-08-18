"""
CODSOFT - Python Programming Internship
Task 4: Rock-Paper-Scissors Game

"""
import random

choices = ["rock", "paper", "scissors"]

user_score = 0
computer_score = 0

print("=" * 45)
print("       ROCK - PAPER - SCISSORS GAME")
print("=" * 45)

while True:
    print("\nChoose one:")
    print("1. Rock")
    print("2. Paper")
    print("3. Scissors")
    print("4. Quit")

    user_input = input("\nEnter your choice: ").lower().strip()

    if user_input == "4" or user_input == "quit":
        break

    if user_input in ["1", "rock"]:
        user_choice = "rock"
    elif user_input in ["2", "paper"]:
        user_choice = "paper"
    elif user_input in ["3", "scissors"]:
        user_choice = "scissors"
    else:
        print("Invalid choice! Please choose Rock, Paper, or Scissors.")
        continue

    computer_choice = random.choice(choices)

    print("\nYour choice     :", user_choice.capitalize())
    print("Computer choice :", computer_choice.capitalize())

    if user_choice == computer_choice:
        print("Result          : It's a TIE!")

    elif (
        (user_choice == "rock" and computer_choice == "scissors")
        or
        (user_choice == "paper" and computer_choice == "rock")
        or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        print("Result          : YOU WIN! ")
        user_score += 1

    else:
        print("Result          : COMPUTER WINS!")
        computer_score += 1

    print("\nScore:")
    print("You      :", user_score)
    print("Computer :", computer_score)

    play_again = input("\nDo you want to play again? (yes/no): ").lower().strip()

    if play_again != "yes" and play_again != "y":
        break

print("\n" + "=" * 45)
print("             FINAL SCORE")
print("=" * 45)
print("Your Score     :", user_score)
print("Computer Score :", computer_score)

if user_score > computer_score:
    print("Overall Winner : YOU! ")
elif computer_score > user_score:
    print("Overall Winner : COMPUTER!")
else:
    print("Overall Result : TIE!")

print("\nThank you for playing!")
