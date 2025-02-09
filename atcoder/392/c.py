N = int(input())
P = list(map(int,input().split()))
Q = list(map(int,input().split()))

person_and_zekken = {}
for i in range(N):
  person_and_zekken[Q[i]] = i +1

result = [0] * N
for i in range(1,N + 1):
  person = person_and_zekken[i]
  target_person = P[person - 1]
  result[i - 1] = Q[target_person -1]

print(' '.join(map(str, result)))