print("Guessing game one to Thousand")
print()
number = 736
score = 0
while True:
  Guess = int(input("Guess the number: "))
  score += 1
  if Guess <= 0:
    exit("Meh >:(")
  elif Guess == number:
    print("You guessed the number correctly! it took you", score, "attempts.")
    exit()
  elif Guess > number:
    print("That's too high!")
    continue
  elif Guess < number:
    print("That's too low!")
    continue
