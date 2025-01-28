N = int(input())
A = list(map(int,input().split()))

a = A[0]

limit = min(A)

for i in range(2,len(A)):
    current = A[i]

    for j in range(limit):
        if a % j == 0 and current % j == 0:
            result = j
     