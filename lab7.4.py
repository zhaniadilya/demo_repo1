n = int(input("Zhumysshylar sany: "))
demalystar = {}

for i in range(n):
    name, day, month = input().split()
    if month not in demalystar:
        demalystar[month] = [name]
    else:
        demalystar[month].append(name)

ai_demalys = input("Aidy engiziniz: ")
if ai_demalys in demalystar:
    print('{} demaldy - {}'.format(" ".join(ai_demalys, demalystar[ai_demalys])))
else:
    print()
