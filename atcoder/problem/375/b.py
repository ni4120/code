import math

N = int(input())
X = []
Y = []
for i in range(N):
  x,y = map(int,input().split())
  X.append(x)
  Y.append(y)
  
current_x = 0
current_y = 0
cost = 0

for i in range(N):
  cost += math.sqrt((current_x - X[i]) ** 2 + (current_y - Y[i]) ** 2)
  current_x = X[i]
  current_y = Y[i]
  
cost += math.sqrt((current_x - 0) ** 2 + (current_y - 0) ** 2)
print(cost)