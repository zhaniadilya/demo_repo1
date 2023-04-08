#1-tapsyrma
'''import random
cort1=()
cort2=()
cort3=()
def cort(cort1, cort2, cort3):
    for i in range(10):
        cort1 = tuple(random.randint(0, 5))
        cort2 = tuple(random.randint(-5, 0))
    cort3=cort1+cort2
    res = cort3.count(0)
    print(cort3, f'0-der sany: res')'''

#2-tapsyrma
'''cort = (7, (0.12, (('x+i*y'), ("string", ()))))
print(cort[1][1][1][0])'''

#3-tapsyrma
'''import random
days = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sanday']
expenses = {'Products': [], 'Transport': [], 'Balance': []}

for day in days:
    for i in expenses:
        exp = round(random.uniform(10.0, 1500.0), 1)
        expenses[i].append(exp)

res = 0
for i in expenses:
    res += sum(expenses[i])
    print(f"Expenses for {i}: {round(sum(expenses[i]))}")
print("-----------------------------------")
print(f"Expenses for the week: {round(res)}")'''

#4-tapsyrma
'''names = input("Studentter: ").split()
cort = tuple(names)
print("-ва-men ayaqtalatyn studentter tizimi: ")
for name in cort:
    if 'ва' in name:
        print(name, end=" ")'''

#5-tapsyrma
'''text_kir = input("Kirilica soz: ")

kir_arip = {"а": "a", "ә": "a", "б": "b", "в": "v", "г": "g", "ғ": "g", "д": "d", "ж": "j", "з": "z", "к": "k", "қ": "k", "л": "l", "м": "m", "н": "n", "т": "t", "ұ": "u", "с": "s", "ф": "f", "ы": "y", "п": "p", "р": "r", "о": "o", "ү": "u", "і": "i", "и": "i", "й": "i", "у": "u", "е": "e", "ю": "u", "я": "ya", "ш": "sh",}

text_lat = ""
for char in text_kir:
    if char in kir_arip:
        text_lat += kir_arip[char]
    else:
        print("Qaita engiziniz!")
print(text_lat)'''