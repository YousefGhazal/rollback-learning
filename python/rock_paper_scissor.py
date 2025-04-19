import random

choices = ("r", "p", "s")
names = {"r": "Rock", "p": "Paper", "s": "Scissors"}
while True:
    user_choice = input("Enter your choice (r/p/s): ").lower()
    computer_choice = random.choice(choices)
    if user_choice not in choices:
        print("Invalid choice. Please try again.")
        continue

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
    print(f"you choice {names[user_choice]}")
    print(f"computer choice {names[computer_choice]}")
    play_again = input("want to play again: (y/n)")
    if play_again != "y":
        break
