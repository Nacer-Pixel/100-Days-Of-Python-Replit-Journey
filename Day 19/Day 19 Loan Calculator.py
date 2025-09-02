print("Loan Calculator")
LoanAmount=float(input("Enter your Loan amount: "))
Years=int(input("Enter the amount of years: "))
Percentage=int(input("Enter the interest percentage: "))
Loan = LoanAmount
for counter in range(Years):
  Interest = (Loan*Percentage)/100
  Loan = Loan+Interest
  NewLoan=round(Loan,2)
  print("Year",counter+1,"is",NewLoan)
print()
Interest = NewLoan-LoanAmount
Interest = round(Interest,2)
print("You have paid",Interest,"$ in interest.")