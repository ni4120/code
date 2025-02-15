N, M = map(int, input().split())

edges = set() #速い 

count = 0

for _ in range(M):
    n, m = map(int, input().split())
    
    if n == m:
        count += 1
    else:
        if n > m:
            n, m = m, n
        
        if (n, m) in edges:
            count += 1
        else:
            edges.add((n, m))

print(count)
