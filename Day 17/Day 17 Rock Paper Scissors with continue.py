from getpass import getpass as input

print()
Player1Score = 0
Player2Score = 0
while True:
  if Player1Score == 3 or Player2Score == 3:
    if Player1Score > Player2Score:
      print("Player one score is",Player1Score,"and wins the game!")
      exit()
    elif Player2Score > Player1Score:
      print("Player two score is",Player2Score,"and wins the game!")
      exit()
  Player1 = input("What is your move? Player 1 (R, P or S)")
  Player2 = input("What is your move? Player 2 (R, P or S)")
  if Player1 == Player2:
    print("Its a draw!")
    continue
  #Rock and Paper
  elif Player1 == "R" and Player2 == "P":
    print("Player 2 Wins!")
    Player2Score += 1
    print("Player two score is: ", Player2Score)
    continue
  elif Player1 == "P" and Player2 == "R":
    print("Player 1 Wins!")
    Player1Score += 1
    print("Player one score is: ", Player1Score)
    continue
  #Scissors and Paper
  elif Player1 == "P" and Player2 == "S":
    print("Player 2 Wins!")
    Player2Score += 1
    print("Player two score is: ", Player2Score)
    continue
  elif Player1 == "S" and Player2 == "P":
    print("Player 1 Wins!")
    Player1Score += 1
    print("Player one score is: ", Player1Score)
    continue
  #Rock and Scissors
  elif Player1 == "R" and Player2 == "S":
    print("Player 1 Wins!")
    Player1Score += 1
    print("Player one score is: ", Player1Score)
    continue
  elif Player1 == "S" and Player2 == "R":
    print("Player 2 Wins!")
    Player2Score += 1
    print("Player two score is: ", Player2Score)
    continue
  else:
    print("Program failed try again later.")
    continue
