'''
Find the difference between the sum of the squares of the first one hundred natural numbers and the square of the sum.
'''

n1 = 0
for i in range(101):
    n1 +=  i ** 2

n2 = 0
for j in range(101):
    n2 += j

n2 = n2 ** 2

result = n2 - n1
print(result)
