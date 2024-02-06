import random

def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value,max_value)

    return roll 

while True:
    players = input("Enter the number of players (1-4): ")
    if player.isdigit():
        player = int(players)
        if 1 <= player <= 4:
            break
        else:
            print('Invalid, try again')