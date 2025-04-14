import random 

num = random.randint(1, 100)

while True : 
    try: 
        guess = int(input("guess a number between 1 and 100: "))
        if guess > num: 
            print("guess lower")
        elif guess < num:
            print("guess higher")
        else :
            print("you guessed it right")
            break
    except ValueError:
        print ("invalid input")
        