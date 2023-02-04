#1-tapsyrma
"""a = int(input('a = '))
b = int(input('b = '))
if a <= b:
    for i in range(a, b+1):
        print(i, end=' ')
else:
    print('a men b manderin qaita engiziniz, a >= b!')"""

#2-tapsyrma
a = int(input('a = '))
b = int(input('b = '))
if a < b:
    for i in range(a, b+1):
        print(i, end=' ')
elif a > b:
    for i in reversed(range(b, a+1)):
        print(i, end=' ')
else:
    print('a men b manderi ten!')