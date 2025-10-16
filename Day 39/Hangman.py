import random
import os

mylist = ["music","london","grape","pizza","pineapple","british","evil","mcdonalds","nine","university"]
known = []
lives = 6

myWord = random.choice(mylist)
while True:
  letter = input("\nChoose a letter:").lower()

  if letter in known:
    os.system("clear")
    print("Letter was already found!")
    continue
  if letter in myWord:
    known.append(letter)
    allletters = 1
  print()
  for i in myWord:
    if i in known:
      print(i,end="")
    else:
      print("_",end="")
      allletters = 0

  print()
  if letter not in myWord:
    lives -= 1
    print(f"Incorrect, you have {lives} lives left")
    if lives == 0:
      print("Game over")
      print(f"The word was {myWord}")
      break
  if allletters == 1:
    print(f"Congratulations, you have won the game with {lives} lives left!")