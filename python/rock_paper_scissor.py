import random

ROCK, PAPER, SCISSORS = "r", "p", "s"

names = {ROCK: "Rock", PAPER: "Paper", SCISSORS: "Scissors"}
choices = tuple(names.keys())


def get_user_choice():
    while True:
        user_choice = input("Enter your choice (r/p/s): ").lower()
        if user_choice in choices:
            return user_choice
        else:
            print("Invalid choice.")


def display_choice(user_choice, computer_choice):
    print(f"you choice {names[user_choice]}")
    print(f"computer choice {names[computer_choice]}")


def determine_winner(user_choice, computer_choice):
    if user_choice == computer_choice:
        print("it's tie")
    elif (
        (user_choice == ROCK and computer_choice == SCISSORS)
        or (user_choice == SCISSORS and computer_choice == PAPER)
        or (user_choice == PAPER and computer_choice == ROCK)
    ):
        print("You win")
    else:
        print("You lose!")


def play_game():
    while True:
        user_choice = get_user_choice()
        computer_choice = random.choice(choices)
        display_choice(user_choice, computer_choice)
        determine_winner(user_choice, computer_choice)
        play_again = input("want to play again: (y/n)")
        if play_again != "y":
            break


play_game()
