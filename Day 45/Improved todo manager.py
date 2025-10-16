import os
import time

todolist = []
high = "high"
print("Life Organizer")
print()
print("Welcome to the life organizer.")

def prettyprint():
  print()
  for row in todolist:
    print()
    for i in range(len(row)):
      if i == 0:
        print(f"What is the task >> {row[i]}")
      if i == 1:
        print(f"When is the task >> {row[i]}")
      if i == 2:
        print(f"What is the priority >> {row[i]}")
    print()

def prettyprintpriority():
  for row in todolist:
    for i in range(len(row)):
      if i == 2 and row[i].lower().strip()== "high":
        print()
        print(f"What is the task >> {row[0]}")
        print(f"When is the task >> {row[1]}")
        print(f"What is the priority >> {row[2]}")
    print()

def add():
  if user == "1":
    user_what = input("What is the task ? >> ")
    user_when = input("When is the task ? >> ")
    user_priority = input("What is the priority ? >> ")
    todolistrow = [user_what,user_when,user_priority]
    todolist.append(todolistrow)
    os.system("clear")

def view():
  if user == "2":
    user_menu2 = input("Would you like to? \n1:view all\n2:only view priority\n")
    if user_menu2 == "1":
      prettyprint()
      time.sleep(3)
      os.system("clear")
    if user_menu2 == "2":
      prettyprintpriority()
      time.sleep(3)
      os.system("clear")

def remove():
  if user == "3":
    user_remove = input("What would you like to remove? >>")
    for row in todolist:
      if row[0] == user_remove:
        todolist.remove(row)
        print("Task removed succefully")
        time.sleep(3)
        os.system("clear")
        
def edit():
  if user == "4":
    user_edit = input("What would you like to edit? (task name) >>")
    for row in todolist:
      if row[0] == user_edit:
        todolist.remove(row)
        user_what = input("What is the task ? >> ")
        user_when = input("When is the task ? >> ")
        user_priority = input("What is the priority ? >> ")
        todolistrow = [user_what,user_when,user_priority]          
        todolist.append(todolistrow)
        os.system("clear")

        
while True:
  user = input("What would you like to do? \n1:Add\n2:view\n3:remove\n4:edit\n \n")
  add()
  view()
  remove()
  edit()