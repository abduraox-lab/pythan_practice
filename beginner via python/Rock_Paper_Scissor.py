import random

choices = ["rock", "paper", "scissors"]
while True:
    user = input("Enter Your Choice(rock ,paper , scissors): ").lower()
    if user  not in choices:
        print("Invalid choice please chose fom rock, paper, scissor")
        continue
    print(f"The user chose {user} from choices")
    computer = random.choice(choices)
    print(f"The computer chose {computer} from choices")
    if user == computer:
        print("Draw")
    elif user == "rock" and computer == "scissors":
        print("You won")
    elif user == "paper" and computer == "rock":
        print("You won")
    elif user == "scissors" and computer == "paper":
        print("You won")
    else:
        print("Computer won")

    again = input("Do you want to play again? (yes/no): ").lower()
    if again == "no":
        print("Thank you for playing!")
        break

