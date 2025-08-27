print("Exam Grade Calculator")
print()
print("Name of the exam: Computer Science")
print()
Max = int(input("What is the max possible score? "))
print()
Score = float(input("What is your score? "))
print()
FirstCalc = Score * 100
FinalGrade = FirstCalc / Max
FinalGrade = round(FinalGrade, 2)
if FinalGrade >= 90:
  print("You got", FinalGrade,"% which is a A+")
elif FinalGrade >= 80:
  print("You got", FinalGrade,"% which is a A")
elif FinalGrade >= 70:
  print("You got", FinalGrade,"% which is a B")
elif FinalGrade >= 60:
  print("You got", FinalGrade,"% which is a C")
elif FinalGrade >= 50:
  print("You got", FinalGrade,"% which is a D")
elif FinalGrade >= 40:
  print("You got", FinalGrade,"% which is a U")
else:
  print("You got", FinalGrade,"% .")