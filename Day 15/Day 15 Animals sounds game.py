print("Welcome to the animal world!")
print()
exit = ""
while exit != "yes":
  animal = input("What animal do you want? ")
  if animal == "Cow":
    print("Mooh 🐄")
    exit = input("Would you like to exit? ")
  elif animal == "Cat":
    print("Meow 🐈")
    exit = input("Would you like to exit? ")
  elif animal == "Dog":
    print("Woof 🐕")
    exit = input("Would you like to exit? ")
  elif animal == "Snake":
    print("Ssss 🐍")
    exit = input("Would you like to exit? ")
  elif animal == "Chicken":
    print("Boq boq boq 🐔")
    exit = input("Would you like to exit? ")
  else: 
    print("Try another animal, how about chicken? ")
print("Alright, See you again soon!")