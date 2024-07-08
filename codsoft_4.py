import random

User_Score=0
Computer_Score=0
while True:
    
    user_action = input("Enter a choice rock, paper, scissors: ")
    possible_actions = ["rock", "paper", "scissors"]
    computer_action = random.choice(possible_actions)
    print("\nYou chose", user_action, "computer chose" ,computer_action,".\n")

    if user_action == computer_action:
        print("Both players selected", user_action,". It's a tie!")

    elif user_action == "rock":
        if computer_action == "scissors":
            print("Rock smashes scissors! You win!")
            User_Score += 1
        else:
            print("Paper covers rock! You lose.")
            Computer_Score+=1

    elif user_action == "paper":
        if computer_action == "rock":
            print("Paper covers rock! You win!")
            User_Score+=1
        else:
            print("Scissors cuts paper! You lose.")
            Computer_Score+=1

    elif user_action == "scissors":
        if computer_action == "paper":
            print("Scissors cuts paper! You win!")
            User_Score+=1
        else:
            print("Rock smashes scissors! You lose.")
            Computer_Score+=1

    play=input("\nDo you want to continue ? [Y/N] : ").upper()
    if play=="N":
        print("-----------------------------------------")
        print(f"In Totally\nYou can achieve {User_Score} score.\nThe Computer can achieve {Computer_Score} score.")
        if User_Score>Computer_Score:
            print("In Totally You Win !!!")
        elif User_Score<Computer_Score:
            print("In Totally You Lost !!!")
        else:
            print("In Totally You Equal")
        break