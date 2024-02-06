import random

def roll():
    min_value = 1
    max_value = 6

    # Generate a random number between min_value and max_value
    roll = random.randint(min_value, max_value)

    return roll 

# Get the number of players from user input
while True:
    players = input("Enter the number of players (2 - 4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players")
    else:
        print('Invalid, try again')

max_score = 50
player_scores = [0 for _ in range(players)]

# Continue the game until a player reaches or exceeds max_score
while max(player_scores) < max_score:
    print("\nCurrent max score:", max(player_scores))
    print("Threshold max score:", max_score)
    
    for player_idx in range(players):
        print("\nPlayer number", player_idx + 1, "turn has just started!\n")
        print("Your total score is:", player_scores[player_idx], "\n")
        current_score = 0

        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break   

            value = roll()
            if value == 1:
                print("You rolled a 1! Turn done!")
                current_score = 0
                break
            else:
                current_score += value
                print("You rolled a:", value)
                print("Your score is:", current_score)

        # Update the player's total score
        player_scores[player_idx] += current_score
        print("Your total score is", player_scores[player_idx])

    # Check if any player has reached or exceeded max_score
    max_score_check = max(player_scores)
    if max_score_check >= 50:
        break

# Find the winner and display the result
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print("Player number", winning_idx + 1, "is the winner with a score of:", max_score)
