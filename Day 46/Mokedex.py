print("Mokebeast")
print()
mokemon = {}
def prettyprint():
  for key, value in mokemon.items():
    print(f"{key}: ",end="")
    for subkey, subvalue in value.items():
      print(f" {subkey}: {subvalue} ", end="")
      print()
    print()
while True:
  name = input("Name > ")
  element = input("Element > ")
  starthp = input("Staring HP > ")
  specialmove = input("Special move > ")
  startmp = input("Staring MP > ")
  mokemon[name] = {"Element":element,"Staring HP":starthp,"Special move":specialmove,"Staring MP":startmp}
  print()
  again = input("Again ? (y/n) > ")
  if again == "n":
    print()
    break

prettyprint()

