#1-tapsyrma
about_me = "My name is Zhani Adilya Qanatqyzy I am a student of the Satbayev University I am a 3rd year student in software engineering"
first_list = about_me.split()
new_info = "I do not have work experience yet"
second_list = new_info.split()
#new_list = first_list + second_list
new_list = first_list.extend(second_list)
print(new_list)
print("----------------------------")
second_list = second_list.append("!")
print(second_list)
print("----------------------------")
copy_first_list = first_list.copy()
print("Copied list: ", copy_first_list)
print("----------------------------")
copy_first_list = copy_first_list.reverse()
print(copy_first_list)
print("----------------------------")
copy_first_list.clear()
print("List after clearing: ", copy_first_list)
