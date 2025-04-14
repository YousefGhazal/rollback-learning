import random 

best_score = None 
while True:
    count = 6
    try:
        minimum = int(input("Enter the minimum number: "))
        maximum = int(input("Enter the maximum number: "))
        num = random.randint(minimum, maximum)
    except ValueError:
        print("Invalid input")
        continue

    attempts = 0 

    while count != 0:
        count -= 1
        attempts += 1
        print(f"You have {count} tries left")
        if count == 0:
            print("You lose")
            print(f"The number was {num}")
            break
        try: 
            guess = int(input(f"Guess a number between {minimum} and {maximum}: "))
            if guess > num: 
                print("Guess lower")
            elif guess < num:
                print("Guess higher")
            else:
                print("You guessed it right!")
                if best_score is None or attempts < best_score:
                    best_score = attempts
                print(f"It took you {attempts} attempts.")
                print(f"Best score: {best_score} attempts.")
                break
        except ValueError:
            print("Invalid input")
    
    play_again = input("Do you want to play again? (yes/no): ").strip().lower()
    if play_again != 'yes':
        print("Thanks for playing!")
        print(f"Your best score was: {best_score} attempts.")
        break