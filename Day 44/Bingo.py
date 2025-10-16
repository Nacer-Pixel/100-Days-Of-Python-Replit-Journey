import random

X = "X"
win = 0
randomnum = 0


def ran():
  number = random.randint(1, 90)
  return number


numbers = []
for i in range(8):
  while True:
    randomnum = ran()
    if randomnum in numbers:
      continue
    else:
      numbers.append(randomnum)
      break


def prettyprint():
  for row in bingo:
    for items in row:
      print(f"|{items}|", end="")
    print("\n")


numbers.sort()

bingo = [[numbers[0], numbers[1],
          numbers[2]], [numbers[3], "BINGO", numbers[4]],
         [numbers[5], numbers[6], numbers[7]]]

prettyprint()
bingonum = 0
while True:
  bingonum = int(input("Next Number: "))
  if bingonum < 0 or bingonum > 90:
    print("Invalid number please try again")
  for row in bingo:
    for i in range(len(row)):
      if bingonum == row[i]:
        row[i] = "X"
        print("Item found!")
        win += 1
        print()
      else:
        continue
  prettyprint()
  if win == 8:
    print("We've got a winner !")
    break
