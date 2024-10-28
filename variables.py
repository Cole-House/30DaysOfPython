import math
# Variables in Python
first_name = 'Cole'
last_name = 'House'
country = 'Sweden'
city = 'Malmo'
age = 22
is_married = True
skills = ['HTML', 'CSS', 'JS', 'React', 'Python']
person_info = {
   'firstname':'Cole',
   'lastname':'House',
   'country':'Sweden',
   'city':'Malmo'
   }

# Printing the values stored in the variables

print('First name:', first_name)
print('First name length:', len(first_name))
print('Last name: ', last_name)
print('Last name length: ', len(last_name))
print('Country: ', country)
print('City: ', city)
print('Age: ', age)
print('Married: ', is_married)
print('Skills: ', skills)
print('Person information: ', person_info)

First_name = input('What is your name: ')
Age = input('How old are you? ')

print(First_name)
print(Age)

# Casting: Converting one data type to another data type. We use int(), float(), str(), list, set When we do arithmetic operations string numbers should be first converted to int or float otherwise it will return an error. If we concatenate a number with a string, the number should be first converted to a string. We will talk about concatenation in String section.

# str to list
first_name = 'Asabeneh'
print(first_name)               # 'Asabeneh'
first_name_to_list = list(first_name)
print(first_name_to_list)            # ['A', 's', 'a', 'b', 'e', 'n', 'e', 'h']

radius = 30
area_of_circle = (math.pi * radius ** 2)  