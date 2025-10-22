f = open ("high.score","r")
allscores = []
high = []
best = 0

while True:
  contents = f.readline().strip()
  if contents == "":
    break
  high.append(contents.split()) 

for items, value in high:
  allscores.append(int(value))

allscores.sort()
allscores.reverse()
best = allscores[0]

for items, value in high:
  if int(value) == best:
    print(f"Current leader is {items} {value}")
f.close()