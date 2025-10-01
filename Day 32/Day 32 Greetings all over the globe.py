import random,os

Greetings = ["Hello there!","As-salamu alaykum","Bonjour","Konnichiwa","Namaste","Namaskar","Sain baina uu"]
Languages = ["English","Arabic","French","Japaneese","Nepali","Indian","Mangolian"]

while True:
  Language = random.randint(0,6)
  Question = input("Do you want to know a random greeting from the globe? y/n \n")
  print()
  os.system("clear")
  if Question == "y":
    print(Greetings[Language])
    print()
    reveal = input("Press 1 to reveal \n")
    print()
    if reveal == "1":
      print(Languages[Language])
    else:
      print("Invalid Syntax")
      print()
    continue
  elif Question == "n":
    print("Thanks alot, see you next time")
    exit()