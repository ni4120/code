H, W = map(int, input().split())
S = [input() for _ in range(H)] 

min_row,max_row = H,-1
min_column,max_column = W,-1

for i in range(H):
  for j in range(W):
    if S[i][j] == "#":
      min_row = min(min_row,i)
      max_row = max(max_row,i)
      min_column = min(min_column,j)
      max_column = max(max_column,j)

for i in range(min_row,max_row + 1):
  for j in range(min_column,max_column + 1):
    if S[i][j] == ".":
      print("No")
      exit()

print("Yes")