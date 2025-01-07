N = int(input())
A = list(map(int,input().split()))

gcd = A[0]

for i in range(1,len(A)):
    current = A[i]
    
    while gcd > 0 and current > 0:
        if gcd > current:
            gcd %= current
        else:
            current %= gcd
    
    if gcd > 0:
        gcd = gcd
    else:
        gcd  = current

print(gcd)