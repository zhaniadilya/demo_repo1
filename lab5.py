#1-tapsyrma
"""about_me = "My name is Zhani Adilya Qanatqyzy I am a student of the Satbayev University I am a 3rd year student in software engineering"
first_list = about_me.split()
new_info = "I do not have work experience yet"
second_list = new_info.split()
new_list = first_list + second_list
# new_list = first_list.extend(second_list)
print(new_list)
print("----------------------------")
second_list.append("!")
print(second_list)
print("----------------------------")
copy_first_list = first_list.copy()
print("Copied list: ", copy_first_list)
print("----------------------------")
copy_first_list.reverse()
print(copy_first_list)
print("----------------------------")
copy_first_list.clear()
print("List after clearing: ", copy_first_list)"""

#1-tapsyrma
'''
import random
students = []
classes = [] 
stud_class = []
n = int(input("Students number: "))
for i in range(n):
    stud = []
    print(i, ' student name: ')
    stud.append((input()))
    students.append(stud)
    classes.append(random.randint(9, 11))
    stud_class.append([students, classes])

stud_class.sort(key=lambda x: x[1])

for i in stud_class:
    print(i[0], i[1])
'''
#2-tapsyrma
def students(name):
    student_grade = [
        ['Baqytzhamal', 'WEB', 95],
        ['Nargiza', 'Data Analysis', 93],
        ['Aidana', 'Functional Programming', 94],
        ['Aiymgul', 'RMP', 92]
    ]
    for i in student_grade:
        if i[0] == name:
            return i[2]
name = input("Student's name: ")            
print(students(name)) 

#3-tapsyrma
"""my_list = []

print("Enter the integers (enter 0 to end the list): ")
val = int(input())

while val != 0:
    my_list.append(val)
    val = int(input())

my_list.sort()

print("Sorted list in ascending order: ")
for num in my_list:
    print(num)"""  

#4-tapsyrma
"""import random
ticket_numbers = []

while len(ticket_numbers) < 6:
    random_number = random.randint(1, 49)
    if random_number not in ticket_numbers:
        ticket_numbers.append(random_number)

ticket_numbers.sort()

print("Your ticket numbers are:")
print(ticket_numbers"""

#5-tapsyrma
"""def sort_list(list): 
    if all(list[i] <= list[i + 1] for i in range(len(list)-1)): 
        return True
    else: 
        return False

my_list = [] 
n = int(input("Size of the list: ")) 
for i in range(0, n): 
    numbers = int(input()) 
    my_list.append(numbers)

if sort_list(my_list):
    print("The list is sorted!")
else:
    print("The list is not sorted!")"""