import random #Allows us to generate a random number 

print('Hello Kamal')

#Rock Paper Scissors 
rock = 1 #Assigns rock to 1
paper = 2 #Assigns paper to 2 
scissors = 3 #Assigns scissors to 3 

while True:
    try:
        UserChoice = int(input('Choose either 1 for Rock, 2 for Paper, or 3 for Scissors: '))
    except ValueError:
        print("That's not a number! Please type 1, 2, or 3.")
        continue  # Go back to the top of the loop and ask again
    if UserChoice in (1, 2, 3):
        break  # Valid choice, so leave the loop
    print("Please choose 1, 2, or 3.")

ComputerChoice = random.randint(1,3)

if UserChoice == rock and ComputerChoice == rock:
    print("You both chose rock! Its a Tie!")
elif UserChoice == rock and ComputerChoice == paper:
    print("You chose rock and computer chose paper. You Lose!")
elif UserChoice == rock and ComputerChoice == scissors:
    print("You chose rock and computer chose scissors. You Win!")
elif UserChoice == paper and ComputerChoice == paper:
    print("You both chose paper! Its a Tie!")
elif UserChoice == paper and ComputerChoice == scissors:
    print("You chose paper and computer chose scissors. You Lose!")
elif UserChoice == paper and ComputerChoice == rock:
    print("You chose paper and computer chose rock. You Win!")
elif UserChoice == scissors and ComputerChoice == scissors:
    print("You both chose scissors! Its a Tie!")
elif UserChoice == scissors and ComputerChoice == rock:
    print("You chose scissors and computer chose rock. You Lose!")
elif UserChoice == scissors and ComputerChoice == paper:
    print("You chose scissors and computer chose paper. You Win!")

