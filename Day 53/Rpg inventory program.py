import os,time

inventory = []

try:
  f = open("inventory.txt","r")
  save = eval(f.read())
  inventory = save
  f.close()
except:
  print("",end="")
  
def screenclear(loading):
  if loading == 1:
    for i in range(1,3):
      print(f"Wrong syntax, Please try again {i}")
      time.sleep(1)
      os.system("clear")
  elif loading == 2:
    for i in range(1,3):
      print(f"Item not found, Please try again {i}")
      time.sleep(1)
      os.system("clear")
  elif loading == 3:
    for i in range(1,3):
      print(f"Item was added {i}")
      time.sleep(1)
      os.system("clear")
  elif loading == 4:
    for i in range(1,3):
      print(f"Item was used {i}")
      time.sleep(1)
      os.system("clear")
  elif loading == 5:
    time.sleep(3)
    os.system("clear")


def action_syntax():
  global action
  while True:
    try:
      action = int(input("1: Add\n2: Remove\n3: View\n \n"))
      if action > 3 or action < 0:
        print("Invalid syntax, Please try again.")
        screenclear(1)
        continue
      else:
        break
    except:
      print("Invalid syntax, Please try again.")
      screenclear(1)
      continue
def action_add():
  if action == 1 :
    item = input("Input the item to add: > ")
    inventory.append(item)
    print(f"{item} has been added")
    screenclear(3)
def action_remove():
  if action == 2 :
    item = input("Input the item to use: > ")
    try:
      inventory.remove(item)
      print(f"{item} has been used")
      screenclear(4)
    except:
      screenclear(2)
def action_view():
  if action == 3 :
    item = input("Input the item to view: > ")
    try:
      item_count = inventory.count(item)
      if item_count > 1:
        print(f"You have {item_count} {item}s")
      else:
        print(f"You have {item_count} {item}")
      screenclear(5)
    except:
      screenclear(2)

while True:
  print("RPG Inventory")
  print()
  action_syntax()
  action_add()
  action_remove()
  action_view()

  f = open("inventory.txt","w")
  f.write(str(inventory))
  f.close()
  
