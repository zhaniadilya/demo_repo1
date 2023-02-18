#zholdarmen zhumys zhasaudy uirenu
#1
colors = "red green blue white yellow"
colors_list = colors.split()
print("\nColors: ", colors_list)
#2
menu = "Today's dinner is pizza"
new_menu = menu.replace("pizza", "pasta")
print("\nMenu: ", new_menu)
#3
message = "hello! how are you?"
new_message = message.capitalize()
print("\nMessage: ", new_message)
#4
univer = "SU"
aboutSU = "I am a student of the SU. I like my university. At SU I found a lot of friends. Also I'm getting good knowledge. So I feel happy being student of the SU!" 
print("\n", univer, " sozi ", aboutSU.count(univer), " ret kezdesedi. \n")
#5
sub1 = "Functional Programming"
sub2 = "Web Programming"
number = int(input("Number is "))
if number == 1:
    print(sub1.upper())
elif number == 2:
    print(sub2.lower())
else:
    print("Please return number again!\n")
#6
city1 = "Almaty"
city2 = "Oskemen"
if len(city1) > len(city2):
    print("\n", city1)
else:
    print("\n", city2)
#7
t = "Almaty is a beautiful city. I study at Almaty. I like Almaty!"
t_find = "Almaty"
print("\n", t_find, " sozi birinshi ret ", t.find(t_find), "-nomerinde kezdesedi!")
#8
classmates = {"Akgul", "Zhansaya", "Aiganym"}
friends = {"Aqerke", "Aiganym", "Aiida"}
print("\n", classmates.union(friends))
#9
students = {"Bakytzhamal", "Aidana", "Nargiza", "Aiymgul", "Asel"}
studentGroup = {"Asel", "Aidana"}
print("\n", studentGroup.issubset(students))
#10
name = "My name is ADILYA"
new_name = name.swapcase()
print("\n", new_name)
