print("Welcome to my computer quiz !")

playing = input("Do you want to play? ")

if playing.lower() != "yes":
    quit()

print("okay Lets play");
score = 0;
answer = input("What does GPU stand for? ")
if answer.lower() == "graphics processing unit":
    print("Correct")
    score +=1;
else:
    print("Incorrect")

answer = input("what does CPU stand for? ")
if answer.lower() == "centeral processing unit":
    print("correct")
    score+=1;
else:
    print("Incorrect")

answer = input("what does means AI ? ")
if answer.lower() =="ai":
    print("correct");
    score+=1
else:
    print("Incorrect")

print("Your correct answer is " +str(score) +" questions")

