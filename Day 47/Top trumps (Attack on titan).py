import os
import time

print ("🌟Top Trumps🌟")
print()
print("Welcome to the Top Trumps 'Strongest Titan in attack on titan!' Simulator")
print()

character = {}
versus = "Eggs"
eversus = "Eggs"
stat1 = 0
attacktitan = {"Intelligence":60,"Handsomeness":97,"Power":91,"Height":65}
armoredtitan = {"Intelligence":44,"Handsomeness":68,"Power":89,"Height":54}
femaletitan = {"Intelligence":89,"Handsomeness":99,"Power":86,"Height":63}
colossaltitan = {"Intelligence":98,"Handsomeness":34,"Power":91,"Height":100}
beasttitan = {"Intelligence":96,"Handsomeness":12,"Power":34,"Height":40}
jawltitan = {"Intelligence":46,"Handsomeness":46,"Power":96,"Height":12}
foundingltitan = {"Intelligence":86,"Handsomeness":50,"Power":92,"Height":67}
warhammer = {"Intelligence":78,"Handsomeness":21,"Power":93,"Height":68}
carttitan = {"Intelligence":91,"Handsomeness":23,"Power":56,"Height":29}

character = {"Attack titan": attacktitan,"Armored titan": armoredtitan,"Female titan":femaletitan,"Colossal titan":colossaltitan,"Beast titan":beasttitan,"Jaw titan":jawltitan,"Founding titan":foundingltitan,"War hammer":warhammer,"Cart titan":carttitan}

def fighting():
  os.system("clear")
  print("fighting")
  time.sleep(1)
  os.system("clear")
  print("fighting.")
  time.sleep(1)
  os.system("clear")
  print("fighting..")
  time.sleep(1)
  os.system("clear")
  print("fighting...")
  
print()
while True:
  choose = input("Choose your card :\n1- Attack titan\n2- Armored titan\n3- Female titan\n4- Colossal titan\n5- Cart titan\n6- Beast titan\n7- Jaw titan\n8- Founding titan\n9- War hammer titan\n \n")
  print()
  stat = input("Choose your stat:\n1- Intelligence\n2- Handsomeness\n3- Power\n4- Height\n")
  print()
  enemy = input("Choose your enemy card :\n1- Attack titan\n2- Armored titan\n3- Female titan\n4- Colossal titan\n5- Cart titan\n6- Beast titan\n7- Jaw titan\n8- Founding titan\n9- War hammer titan\n \n")
  print()
  for i in range (1,9):
    if i == int(choose):
      if stat == "1":
        stat = "Intelligence"
      if stat == "2":
        stat = "Handsomeness"
      if stat == "3":
        stat = "Power"
      if stat == "4":
        stat = "Height"
  for i in range (1,9):
    if choose == "1":
      versus = "Attack titan"
    if choose == "2":
      versus = "Armored titan"
    if choose == "3":
      versus = "Female titan"
    if choose == "4":
      versus = "Colossal titan"
    if choose == "5":
      versus = "Cart titan"
    if choose == "6":
      versus = "Beast titan"
    if choose == "7":
      versus = "Jaw titan"
    if choose == "8":
      versus = "Founding titan"
    if choose == "9":
      versus = "War hammer"
  for i in range (1,9):
    if enemy == "1":
      eversus = "Attack titan"
    if enemy == "2":
      eversus = "Armored titan"
    if enemy == "3":
      eversus = "Female titan"
    if enemy == "4":
      eversus = "Colossal titan"
    if enemy == "5":
      eversus = "Cart titan"
    if enemy == "6":
      eversus = "Beast titan"
    if enemy == "7":
      eversus = "Jaw titan"
    if enemy == "8":
      eversus = "Founding titan"
    if enemy == "9":
      eversus = "War hammer"
  stat1 = character[versus][stat]
  stat2 = character[eversus][stat]
  fighting()
  if stat1 > stat2:
    print(f"{versus} has a {stat} stat of {stat1}")
    print(f"{eversus} has a {stat} stat of {stat2}")
    print()
    print(f"{versus} wins!")
  elif stat2 > stat1:
    print(f"{eversus} has a {stat} stat of {stat2}")
    print(f"{versus} has a {stat} stat of {stat1}")
    print()
    print(f"{eversus} wins!")
  elif stat2 == stat1:
    print(f"{eversus} has a {stat} stat of {stat2}")
    print(f"{versus} has a {stat} stat of {stat1}")
    print()
    print("its a tie!")
    print()
  again = input("Again? (y/n) > ")
  if again == "n":
    break