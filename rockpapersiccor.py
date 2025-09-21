import random
ROCK="r"
SCISSORS="s"
PAPER="p"
emojis={"r":"💎","p":"📃","s":"✂"}
choices=tuple(emojis.keys())

def get_user_choice():
    while True:
        user_choice=input("choose(r/p/s):")
        if user_choice in choices:
            return user_choice 
        else:
            print("invalid choice")

def display_choice(user_choice,computer_choice):
    print("your chose: ",emojis[user_choice])
    print("computer chose: ",emojis[computer_choice])

def detemine_winner(user_choice,computer_choice):
    if user_choice==computer_choice:
        print("tie")
    elif (
        user_choice=="r" and computer_choice=="s" or
        user_choice=="s" and computer_choice=="p" or
        user_choice=="p" and computer_choice=="r"):  
        print("you win")
    else:
        print("you lost")

def play_game():
    while True:
        user_choice=get_user_choice()

        computer_choice=random.choice(choices)

        display_choice(user_choice,computer_choice)
        detemine_winner(user_choice,computer_choice)
        
        term=input("do you wanna continue(y/n): ").lower()
        if term=="y":
            print("choose")
        else:
            break
        
play_game()


