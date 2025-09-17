def Dice():
  import random
  Dice8=random.randint(1,8)
  Dice6=random.randint(1,6)
  Stat=Dice6*Dice8
  return Stat

print("Character Stats Generator")
print()
while True:
  Name= input("What is your character name? ")
  print(Name,"'s health is:",Dice(),"hp")
  print()
  Continue = input("Do you have another character? (y/n) ")
  if Continue =="n":
    break