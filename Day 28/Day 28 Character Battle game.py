import random, os, time

round = 0


def DiceStat1():
  Dice12 = random.randint(1, 12)
  Dice6 = random.randint(1, 6)
  Stat = Dice6 * Dice12 / 2 + 10
  return Stat


def DiceStat2():
  Dice12 = random.randint(1, 12)
  Dice6 = random.randint(1, 6)
  Stat = Dice6 * Dice12 / 2 + 10
  return Stat


def DiceHP1():
  Dice12 = random.randint(1, 12)
  Dice6 = random.randint(1, 6)
  HP = Dice6 * Dice12 / 2 + 12
  return HP


def DiceHP2():
  Dice12 = random.randint(1, 12)
  Dice6 = random.randint(1, 6)
  HP = Dice6 * Dice12 / 2 + 12
  return HP


Character2HP = DiceHP2()
Character1HP = DiceHP1()
Character1Stat = DiceStat1()
Character2Stat = DiceStat2()


os.system("clear")
Character = input("Name your character! ")
os.system("clear")
type = input("Character type?! (Human, Elf, Wizard, Orc) ")
os.system("clear")


Tale = "{} The {}".format(Character,type)
print(Tale)
print("Health: ", Character1HP)
print("Strength: ", Character1Stat)
print()
print("May your name go down in Legend...")
time.sleep(3)


os.system("clear")
print("Who are they batteling?")
print()
Character2 = input("Name your Legend: ")
os.system("clear")
type2 = input("Character type?! (Human, Elf, Wizard, Orc) ")
os.system("clear")
Tale2 = "{} The {}".format(Character2,type2)
print(Tale2)
print("Health: ", Character2HP)
print("Strength: ", Character2Stat)
print()
print("May your name go down in Legend...")
time.sleep(3)


if Character1Stat > Character2Stat:
  dam = Character1Stat - Character2Stat + 1
else:
  dam = Character2Stat - Character1Stat + 1
while True:
  os.system("clear")
  print("⚔️ BATTLE TIME ⚔️")
  print()
  round += 1
  print("Round", round, "begins!")
  time.sleep(1)
  diceBat1 = random.randint(1, 6)
  diceBat2 = random.randint(1, 6)

  
  if diceBat1 > diceBat2:
    print(Tale, "wins round", round, "!")
    print()
    time.sleep(1)
    print(Tale2, "takes a hit, with", dam, "dammage")
    print()
    Character2HP -= dam
    time.sleep(1)
    if Character2HP <= 0:
      print("Oh no", Tale2, "has died")
      print()
      print(Tale, "Has won the battle in", round, "rounds!")
      exit()
    print(Character2)
    print("HEALTH: ", Character2HP)
    time.sleep(4)

  
  elif diceBat2 > diceBat1:
    print(Tale2, "wins round", round, "!")
    print()
    time.sleep(1)
    print(Tale, "takes a hit, with", dam, "dammage")
    print()
    Character1HP-=dam
    time.sleep(1)
    if Character1HP <= 0:
      print("Oh no", Tale, "has died")
      print()
      print(Tale2, "Has won the battle in", round, "rounds!")
      exit()
    print(Tale)
    print("HEALTH: ", Character1HP)
    time.sleep(4)

  
  else:
    print("Round", round, "terminates in a draw!")
    time.sleep(4)
