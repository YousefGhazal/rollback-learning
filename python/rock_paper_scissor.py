import random

choices = ("r", "p", "s")
names = {"r": "Rock", "p": "Paper", "s": "Scissors"}


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
        (user_choice == "r" and computer_choice == "s")
        or (user_choice == "s" and computer_choice == "p")
        or (user_choice == "p" and computer_choice == "r")
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
