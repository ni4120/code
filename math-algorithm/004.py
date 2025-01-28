# q004
a,b,c = map(int,input().split())
result = a * b * c

print(result)

# q005
a = list(map(int,input().split()))

sum = 0
for i in a:
    sum += i

result = sum % 100
print(result)