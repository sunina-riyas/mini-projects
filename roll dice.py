import random

while True:
    choice=input("enter your choice: ").lower()
    if choice=="y":
        dice1=random.randint(1,6)
        dice2=random.randint(1,6)
        print(dice1,dice2)
    elif choice=="n":
        print("thanks....")
        break
    else:
        print("invalid choice")

