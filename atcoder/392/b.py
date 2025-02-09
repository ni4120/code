N,M = map(int,input().split())
A = list(map(int,input().split()))

result = []

for i in range(N+1):
  if i not in A and i != 0:
    result.append(i)

print(len(result))
print(' '.join(map(str, result)))


