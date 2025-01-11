"""# list comprehension
number = [1,2,3]
add_numb = [n+1 for n in number]
print(add_numb)

name = "kazim"
letter_list = [letter for letter in name]
print(letter_list)

new_list = [n*2 for n in range(5)]
print(new_list)

# conditional list comprehension
names=('John','Andy','Joe','Smith','Williams')
neW_list_of_name = [name for name in names if len(name)==4]
new_list_of_name = [name.upper() for name in names if len(name)>4]
print(neW_list_of_name)
print(new_list_of_name)
"""

# dictionary comprehensive
import random
names=('John','Andy','Joe','Smith','Williams')
new_dict = {student : random.randint(1,100) for student in names}
print(new_dict)
passed_dict = {student : score for (student,score) in new_dict.items() if score>=32}
print(passed_dict)