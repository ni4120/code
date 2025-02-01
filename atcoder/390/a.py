a = list(map(int, input().split()))

target = [1, 2, 3, 4, 5]

for i in range(4):
    a[i], a[i + 1] = a[i + 1], a[i] 
    if a == target:
        print("Yes")
        exit()
    a[i], a[i + 1] = a[i + 1], a[i] 

print("No")
