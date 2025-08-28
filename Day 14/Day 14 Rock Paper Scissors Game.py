from getpass import getpass as input

print()
Player1 = input("What is your move? Player 1 (R, P or S)")
Player2 = input("What is your move? Player 2 (R, P or S)")
if Player1 == Player2:
  print("Its a draw!")
#Rock and Paper 
elif Player1 == "R" and Player2 == "P":
  print("Player 2 Wins!")
elif Player1 == "P" and Player2 == "R":
  print("Player 1 Wins!")
#Scissors and Paper 
elif Player1 == "P" and Player2 == "S":
  print("Player 2 Wins!")
elif Player1 == "S" and Player2 == "P":
  print("Player 1 Wins!")
#Rock and Scissors 
elif Player1 == "R" and Player2 == "S":
  print("Player 1 Wins!")
elif Player1 == "S" and Player2 == "R":
  print("Player 2 Wins!")
else:
  print("Program failed try again later.")