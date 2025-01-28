#q018
#全探索
n = int(input())
A = list(map(int,input().split()))

count = 0
for i in range(n-1):
    for j in range(n-2):
        if A[i] + A[j] == 500:
            count += 1

print(count)

#改
n = int(input())
A = list(map(str,input().split()))

one = A.count("100")
two = A.count("200")
three = A.count("300")
four = A.count("400")

num1 = one * four
num2 = two * three

print(num1 + num2)

#q019
n = int(input())
A = list(map(int,input().split()))

red = A.count(1)
yellow = A.count(2)
blue = A.count(3)

result = 0

if red > 0:
    red_c = (red * red -1) // 2
    result += red_c
if yellow > 0:
    yellow_c = (yellow * yellow -1) // 2
    result += yellow_c
if blue > 0:
    blue_c = (blue * blue -1) // 2
    result += blue_c

print(result)