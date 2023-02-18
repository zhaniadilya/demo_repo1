my_text = input("Sozdi engiziniz: ")
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
    print("Kishi zhane ulken arip sany ten!")