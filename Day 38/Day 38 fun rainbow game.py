sentence = input("What is the sentence you would like to rainbow spray? ")

for letters in sentence:
  if letters.lower()== "r":
    print(f"\033[31m{letters}", end="")
  elif letters.lower()== "b":
    print(f"\033[34m{letters}", end="")
  elif letters.lower()== "m" or letters.lower() == "p":
    print(f"\033[35m{letters}", end="")
  elif letters.lower()== "g":
    print(f"\033[32m{letters}", end="")
  elif letters.lower()== "y":
    print(f"\033[33m{letters}", end="")
  elif letters.lower()== "c":
    print(f"\033[36m{letters}", end="")
  elif letters.lower()== " ":
    print(f"\033[0m{letters}", end="")
  else:
    print(f"{letters}", end="")