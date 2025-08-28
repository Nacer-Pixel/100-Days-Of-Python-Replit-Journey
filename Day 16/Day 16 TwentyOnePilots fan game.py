Game_start = input("Are you a true Twenty One Pilot fan ? ")
ChlorineAttempt = 0
if Game_start == "yes" or Game_start == "Yes":
  print("Then fill in these gaps ")
  while True:
    ChlorineAnswer = input("Sippin' on straight ________ ")
    ChlorineAttempt += 1
    if ChlorineAnswer == "chlorine":
      break
    print("Nope try again!")
  print("Well done it took you", ChlorineAttempt, "attempts")
  Round_Two = input("Do you want to continue ? ")
  RideAttempt = 0
  if Round_Two == "yes" or Round_Two == "Yes":
    print("Then fill in these gaps ")
    while True:
      RideAnswer = input("I’m falling so I’m ______ my time on my ride, ")
      RideAttempt += 1
      if RideAnswer == "taking":
        break
      print("Nope try again!")
    print("Well done it took you", RideAttempt, "attempts")
  Round_Three = input("Do you want to continue ? ")
  JumpsuitAttempt = 0
  if Round_Three == "yes" or Round_Three == "Yes":
    print("Then fill in these gaps ")
    while True:
      JumpsuitAnswer = input("Jumpsuit, ________ cover me, ")
      JumpsuitAttempt += 1
      if JumpsuitAnswer == "Jumpsuit" or JumpsuitAnswer == "jumpsuit":
        break
      print("Nope try again!")
    print("Well done it took you", JumpsuitAttempt, "attempts")
  Total = JumpsuitAttempt + RideAttempt + ChlorineAttempt
  Mistakecount = Total - 3
  if Total == 3:
    print("Well done you have finished the game without any mistake!")
  else:
    print("Well done you have completed the game with", Mistakecount,
          "mistakes")
else:
  print("We only accept TOP fans to play our game, sorry.")
