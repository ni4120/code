N = int(input())

S = []
for i in range(N):
  s = input()
  S.append(s)
  
sorted_words = sorted(S,key = len)
result = ""
for i in range(N):
  result += sorted_words[i]
  
print(result)