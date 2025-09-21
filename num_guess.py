import random

num=random.randint(1,50)

while True:
    try:
        guess=int(input("enter your guess: "))
        if guess<num:
                    print("too low")
        elif guess>num:
                    print("too high")    
        else:
                    print("your guessed is right")
                    break          
    except ValueError:
        print("please enter a valid number")
