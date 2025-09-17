print("Math game!")
print()
score = 0
Multiples = int(input("Name your multiples: "))
print()
for i in range(1,11):
  Question = Multiples*i
  print(i,"X",Multiples,"=")
  Answer=int(input())
  if Answer == Question:
    print()
    print("Correct!")
    print()
    score+=1
    continue
  else:
    print()
    print("Wrong the answer was",Question)
    print()
    continue

print("You scored",score,"out of 10!")