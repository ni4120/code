'''
2520 is the smallest number that can be divided by each of the numbers from 1 to 10 without any remainder.
What is the smallest positive number that is evenly divisible by all of the numbers from 1 to 20?
最少公倍数を求める
'''
'''

limit = 20
num = limit #10で割れるのは10以上

while True:
    for i in range(1,limit + 1 ):
        if num % i != 0:
            break
    else:
        result = num
        break
    num = num + 1


print(result)

'''
import math

def lcm(a, b):
    return abs(a*b) // math.gcd(a, b)

limit = 20
result = 1

for i in range(1, limit + 1):
    result = lcm(result, i)

print(result)
