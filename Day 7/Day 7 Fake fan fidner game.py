print("Fake Fan Finder")
print()
Anime = input("What's your favorite anime? ")
if Anime == "Attack on titan":
  print("Great choice, Now lets test your knowledge!")
  print()
  Hero = input("Whats the main character first name? ")
  if Hero == "Eren":
    print("Correct! Now you're a training camp initiate")
    City = input("Where was eren born? ")
    if City == "Shiganshina":
      print("Wonderful! Now you're a training camp graduate")
      LastName = input("What's Eren's last name? ")
      if LastName == "Jeager":
        print("Correct! You joined the Scouting Legion")
      elif LastName == "Yeager":
        print(
            "The correct answer is Jeager but i'll let it slide this time :/ ")
        print(
            "Congratulations! You have passed the Real Fan exam, And have joined levi's squad"
        )
      else:
        print("FAKE FAN GO AWAY!")
    else:
      print("FAKE FAN GO AWAY!")
  else:
    print("FAKE FAN GO AWAY!")
else:
  print("Mid show, you should watch Attack on titan.")
