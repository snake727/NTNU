#Import libary
import random as r

#Define values
actions = ["rock", "paper", "scissor"]

#Generate what move the computer will choose
computerHand = r.choice(actions)

while True:
    try:
        playerHand = input("Input the move you wish to play (rock, paper or scissor): ")
        while playerHand not in ["rock", "paper", "scissor"]:
            print("Input is invalid!")
            playerHand = input("Input the move you wish to play (rock, paper or scissor): ")
        if playerHand == computerHand:
            print(f"You choose {playerHand} and the computer chooses {computerHand}, it's a tie!")
        elif playerHand == "rock":
            if computerHand == "scissor":
                print(f"You choose {playerHand}, which destroys computer's choice: {computerHand}! You win!")
            else:
                print(f"You choose {playerHand}, but computer covers you up with {computerHand}! You lose!")
        elif playerHand == "paper":
            if computerHand == "rock":
                print(f"You choose {playerHand}, which covers up computers choice: {computerHand}. You win!")
            else:
                print(f"You choose {playerHand}, but the computer cuts you into pieces with {computerHand}! You lose!")
        elif playerHand == "scissor":
            if computerHand == "paper":
                print(f"You choose {playerHand}, which tears through computers choice: {computerHand}! You win!")
            else:
                print(f"You choose {playerHand}, but the computer smashes you with {computerHand}! You lose!")
        break
    except:
        print("You must input a valid move!")