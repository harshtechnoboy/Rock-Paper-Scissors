import random

user_wins = 0 #creating a variable to keep score of the user

computer_wins = 0 #creating a variable to keep score of the computer

options = ["rock" , "paper" , "scissors"] #creating a list for options to choose in the game
            #0         1           2 

while True:
    user_input = input("Type Rock/Paper/Scissors or Q to quit:").lower()
        
    if user_input == "q":
        break

    if user_input not in options:
        continue
            
    random_number = random.randint(0 , 2) # rock is 0 , paper is 1 , scissors is 2

    computer_chooses = options[random_number] #randomly chooses an option on behalf of the computer

    print("Computer chooses", computer_chooses + ".")

    if user_input == "rock" and computer_chooses == "scissors":

        print("You Won!")

        user_wins += 1 #increments users score by 1
        
    elif user_input == "paper" and computer_chooses == "rock":

        print ("You Won!")

        user_wins += 1 #increments users score by 1

    elif user_input == "scissors" and computer_chooses == "paper":
        
        print ("You Won!")

        user_wins += 1 #increments users score by 1

    else:
        print ("You Lost :( ")

        computer_wins += 1 #increments computers score by 1
        
        
print ("You Won" + str(user_wins) + "times.") #displays total score of the user

print ("The Computer Won :(" + str(computer_wins) + "times.") #displays total score of the computer

print("Goodbye!")
