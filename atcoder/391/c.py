N, Q = map(int, input().split())

location = list(range(N + 1))
nest_count = [1] * (N + 1)
multi_nest = 0

for _ in range(Q):
    query = input().split()
    
    if query[0] == "1":
        P, H = int(query[1]), int(query[2])
        old_nest = location[P]
        location[P] = H


        if nest_count[old_nest] == 2:
            multi_nest -= 1 
        nest_count[old_nest] -= 1

        if nest_count[H] == 1:
            multi_nest += 1
        nest_count[H] += 1

    else:
        print(multi_nest)
