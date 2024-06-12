'''
What is the largest prime factor of the number 600851475143?
'''

num = 13195
i = 2 
arr = []

while i < num:
    while num % i == 0:
        arr.append(i)
        num //= i   #numをiで÷。numはiで割った商に更新'
    i += 1
if num > 1:    #ループ終了後num>1の場合そのnumは素数
    arr.append(num)


result = arr[-1]
print(result)


'''
num = 13195
i = 2 
arr = []

while i < num:
    while num % i == 0:
        arr.append(i)
        print(f'素因数 {i} を見つけました。num を割ります。新しい num は {num // i} です。')
        num //= i   # numをiで割る。numはiで割った商に更新
    i += 1
    print(f'i をインクリメントします。新しい i は {i} です。')

if num > 1:    # ループ終了後num>1の場合そのnumは素数
    arr.append(num)
    print(f'最後の素因数 {num} を追加します。')

result = arr[-1]
print(f'最大の素因数は {result} です。')

'''