print("ROCK PAPER SCISSORS")
player1 = input("Player 1 Name : ")
player2 = input("Player 2 Name : ")

plays = ["rock", "paper", "scissors"]

player1_Play = input(f"{player1} Is your turn : ")
player2_Play = input(f"{player2} Is your turn : ")

#game logics
if player1_Play == "rock" and player2_Play == "rock":
    print("Draw")
elif player1_Play == "rock" and player2_Play == "paper":
    print(f"{player2} wins")
elif player1_Play == "rock" and player2_Play == "scissors":
    print(f"{player1} wins")
elif player1_Play == "paper" and player2_Play == "rock":
    print(f"{player1} wins")
elif player1_Play == "paper" and player2_Play == "paper":
    print("Draw")
elif player1_Play == "paper" and player2_Play == "scissors":
    print(f"{player2} wins")
elif player1_Play == "scissors" and player2_Play == "rock":
    print(f"{player2} wins")
elif player1_Play == "scissors" and player2_Play == "paper":
    print(f"{player1} wins")
elif player1_Play == "scissors" and player2_Play == "scissors":
    print("Draw")
else:
    print("Invalid Input")
