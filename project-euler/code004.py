'''
A palindromic number reads the same both ways. 
The largest palindrome made from the product of two 2-digit numbers is 9009=91*99.
Find the largest palindrome made from the product of two 3-digit numbers.
'''


arr = []

for i in range(100, 1000):
    for j in range(100, 1000):
        num = i * j
        string = str(num)
        if string == string[::-1]:
            arr.append(num) #数値の方をリストに追加

result = max(arr) #配列の最大値を取得
print(result)

