import os
todolist = []
def printitems():
  for item in todolist:
    print(item)
    print()

def clearscreen():
  while True:
    menu = input("Click 1 to go back to the menu\n")
    if menu == "1":
     os.system("clear")
     break
      
while True:
  print("Dynamic Todo List")
  print()
  action = input("Do you want to view, add, edit, or remove an item from the to do list?\n")
  if action == "view":
    print()
    printitems()
    clearscreen()

  
  elif action == "add":
    print()
    item = input("What would you like to add? \n")
    if item in todolist:
      print("this item is already added!")
      clearscreen()
      os.system("clear")
    else:
      todolist.append(item)
      print("Item added succesfully")
      clearscreen()

  
  elif action == "remove":
    print()
    item = input("What would you like to remove? \n")
    print()
    if item in todolist:  
      decision = input(f"are you sure you would like to remove {item}? (y/n)\n")
      if decision == "y":
        todolist.remove(item)
        os.system("clear")
      else:
        clearscreen()
    else:
      print("Item was not found, please try again.")
      clearscreen()

  elif action == "change" or action == "edit":
    item = input ("Which item would you like to edit?\n")
    if item in todolist: 
      todolist.remove(item)
      Newitem = input("Input your edit:\n")
      todolist.append(Newitem)
      print("Item edited succesfully")
      clearscreen()
    else:
      print("Item was not found")
      clearscreen()
  
  elif action == "erase":
    for item in todolist:
      todolist.remove(item)
      print("Todo list was fully erased!")
      clearscreen()
