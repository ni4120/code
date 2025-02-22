S = input()

kakko = {')': '(', ']': '[', '>': '<'}
count = []

for char in S:
    if char in kakko.values():
        count.append(char)
    elif char in kakko.keys():
        if not count or count[-1] != kakko[char]:
            print("No")
            exit()
        count.pop()

if not count:
  print("Yes")
else:
  print("No")
