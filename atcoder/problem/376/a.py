N,C = map(int,input().split())
T = list(map(int,input().split()))

count = 0
for i in range(N):
  if i == 0 :
    count += 1
    give_time = T[i]
  elif T[i] - give_time < C:
    continue
  elif T[i] - give_time >= C:
    count += 1
    give_time = T[i]
print(count)