import random

number = input("how many time do you want to roll the dice? ")
count = 0
try:
    number = int(number)
    while number != 0:
        number -= 1
        roll = input("roll the dice? (y/n): ").lower()
        if roll == "y":
            count += 1
            dice1 = random.randint(1, 6)
            dice2 = random.randint(1, 6)
            print(f"{dice1} , {dice2}")
        elif roll == "n":
            print("bye bye")
            break
        else:
            print("invalid input")
    print(f"you rolled the dice {count} times")
except ValueError:
    print("invalid input")
