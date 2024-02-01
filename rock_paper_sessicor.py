import random ;

user_win =0;
computer_win =0;

option = ['rock','paper','scissor']

while True:
    user_input = input("Type Rock / Paper /scissor or Q to quit:  ").lower()
    if user_input == 'q':
        break
    if user_input not in option:
        continue

    random_number = random.randint(0,2)
    #rock=1, paper=2, scissor=3
    computer_pick =option[random_number]
    print('computer picked',computer_pick + ".")

    if user_input == "rock" and computer_pick == "scissor":
        print("You Won !! ")
        user_win +=1;
    
    elif user_input == "paper" and computer_pick == "rock":
        print("You Won !!")
        user_win +=1;
      
    elif user_input == "scissor" and computer_pick == "paper":
        print("You Won !!")
        user_win +=1
    else:
        print("You lost!")
        computer_win+=1;

print("You Won ", user_win , "times.")
print("Comouter won",computer_win, "times.")
print('Goodbye!')