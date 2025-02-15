S = list(input())

position_A = []
position_B = []
position_C = []

for i in range(len(S)):
    if S[i] == "A":
        position_A.append(i)
    elif S[i] == "B":
        position_B.append(i)
    elif S[i] == "C":
        position_C.append(i)

count = 0

for i in position_A:
    for j in position_B:
        for k in position_C:
            if i < j < k and (j - i) == (k - j):
                count += 1

print(count)
