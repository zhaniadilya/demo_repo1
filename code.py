#1-tapsyrma
"""a = int(input('a = '))
b = int(input('b = '))
if a <= b:
    for i in range(a, b+1):
        print(i, end=' ')
else:
    print('a men b manderin qaita engiziniz, a >= b!')"""

#2-tapsyrma
"""a = int(input('a = '))
b = int(input('b = '))
if a < b:
    for i in range(a, b+1):
        print(i, end=' ')
elif a > b:
    for i in reversed(range(b, a+1)):
        print(i, end=' ')
else:
    print('a men b manderi ten!')"""

#3-tapsyrma
"""a = int(input('a = '))
b = int(input('b = '))
if(a>b):
    for i in range(a-(a+1)%2, b-b%2, -2):
        print(i, end=' ')
else:
    print("a = b nemese a < b")"""

#4-tapsyrma
n = int(input('N = '))
k = 0
for i in range(1, n+1):
    k+=i
print("Bar kartalardyn manin engiziniz: ")
for i in range(n-1):
    k -= int(input())
print("Zhogalgan karta: ", k)
