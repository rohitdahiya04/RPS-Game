import random

options = ("rock","paper","scissors")
running = True

while running:
    player = None
    computer = random.choice(options)

    while player not in options:
        player = input("Enter your choice (rock, paper, scissors): ")

    print(f"Player:{player}")
    print(f"Computer:{computer}")

    if player == computer:
        print("It's a Tie")
    elif player == "rock" and computer == "scissors":
        print("Player WON")
    elif player == "paper" and computer == "rock":
        print("Player WON")
    elif player == "scissors" and computer == "paper":
        print("Player WON")
    else:
        print("You LOSE")

    play_again = input("Play again (Y/N): ").lower()
    if not play_again == 'y':
        running = False
    
print("Thanks for playing")