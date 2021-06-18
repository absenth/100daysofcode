# 100 Days Of Code - Rock Paper Scissor

import random


def main():
    rps = ["r", "p", "s"]
    print("Welcome to 100 Days Of Code Day 4")
    print("Let's play Rock Paper Scissors!")
    print("")
    player_input = input("Pick Rock, Paper or Scissors ")
    player_rps = player_input.lower().strip()
    computer_rps = random.choice(rps)

    # For Debugging
    print(f"Player picked {player_rps}, computer picked {computer_rps}")

    if player_rps == computer_rps:
        draw(computer_rps)
    elif player_rps == "r" and computer_rps == "p":
        computer_wins(computer_rps)
    elif player_rps == "r" and computer_rps == "s":
        player_wins(computer_rps)
    elif player_rps == "p" and computer_rps == "s":
        computer_wins(computer_rps)
    elif player_rps == "p" and computer_rps == "r":
        player_wins(computer_rps)
    elif player_rps == "s" and computer_rps == "r":
        computer_wins(computer_rps)
    else:
        player_wins(computer_rps)


def computer_wins(computer_rps):
    """ computer wins function """
    print(f"The computer bested you with it's selection of {computer_rps}")
    print("Better luck next time")


def player_wins(computer_rps):
    """ player wins function """
    print(f"You have beaten the computer's {computer_rps}")
    print("Congrats! You Win!")


def draw(computer_rps):
    """ noone wins function """
    print(f"You both chose {computer_rps}")


if __name__ == "__main__":
    main()
