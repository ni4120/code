N = int(input())
A = list(map(int, input().split()))

ratio = A[1] / A[0]

for i in range(1, N):
    if A[i] != A[i - 1] * ratio:
        print("No")
        exit()

print("Yes")
