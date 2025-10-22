n = int(input("Input a number > "))
def factorial(n):
  if n == 1:
    return 1
      # Base case: return something
  else:
    return n*factorial(n-1)
result = factorial(n)
print(result)