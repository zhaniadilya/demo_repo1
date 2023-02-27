#1
"""my_text = input("Sozdi engiziniz: ")
lowerCount = 0
upperCount = 0
for word in my_text:
    if word.islower():
        lowerCount += 1
    elif word.isupper():
        upperCount += 1
    
if lowerCount > upperCount:
    print(my_text.lower())
elif lowerCount < upperCount:
    print(my_text.upper())
else:
    print("Kishi zhane ulken arip sany ten!")"""

#2
while True: 
    num1 = input("Birinshi san: ")
    if num1.isdigit(): 
        num1 = int(num1)
        break
    else:
        print("Kate!")

while True: 
    num2 = input("Ekinshi san: ")
    if num2.isdigit(): 
        num2 = int(num2)
        break
    else:
        print("Kate!")

sum = num1 + num2

print("Summa: " + str(sum))
