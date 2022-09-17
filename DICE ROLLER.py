import random

def rolldice(min,max):
    while True:
        print("Rolling dice....")
        number = random.randint(min,max)
        print(f"Your number : {number}")
        choice = input("Do you want to roll the dice again? (y/n)")
        if choice.lower() == 'n':
            break
rolldice(1, 6)
# change the 1 and 6 to the min and max number you want it
