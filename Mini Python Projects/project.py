import random

def roll():
    min_value = 1
    max_value = 6

    roll = random.randint(min_value,max_value)

    return roll 

players = input("Enter the number of players (1-4): ")