# in order to handle repetitive task programming languages use loops. Python programming language also provides the following types of two loops: while loop AND for loop 
  # syntax
# while condition:
#     code goes here
count = 0
while count < 5:
    print(count)
    count = count + 1
#prints from 0 to 4
# In the above while loop, the condition becomes false when count is 5. That is when the loop stops. If we are interested to run block of code once the condition is no longer true, we can use else.
count = 0
while count < 5:
    print(count)
    count = count + 1
else:
    print(count)
# Break and continue - break statement is used to exit the loop. The continue statement is used to skip the current iteration, and continue with the next.
count = 0
while count < 5:
    print(count)
    count = count + 1
    if count == 3:
        break
# The above while loop only prints 0, 1, 2, but when it reaches 3 it stops.
count = 0
while count < 5:
    if count == 3:
        count = count + 1
        continue
    print(count)
    count = count + 1
# The above while loop only prints 0, 1, 2 and 4 (skips 3).

# For loop - for loop is used to iterate over a sequence (list, tuple, string) or other iterable objects. The syntax of the for loop is as follows:
# for loop with list 
# syntax
# for iterator in lst:
#     code goes here
numbers = [0, 1, 2, 3, 4, 5]
for number in numbers: # number is temporary name to refer to the list's items, valid only inside this loop
    print(number)       # the numbers will be printed line by line, from 0 to 5
#  you can also iterate over a string
language = 'Python'
for letter in language:
    print(letter)
# example with dictionary
person = {
    'first_name':'Asabeneh',
    'last_name':'Yetayeh',
    'age':250,
    'country':'Finland',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address':{
        'street':'Space street',
        'zipcode':'02210'
    }
}
for key in person:
    print(key)

for key, value in person.items():
    print(key, value) # this way we get both keys and values printed out
# loops in a set
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
for company in it_companies:
    print(company)
# In this example below, if the number equals 3, the step after the condition (but inside the loop) is skipped and the execution of the loop continues if there are any iterations left.
numbers = (0,1,2,3,4,5)
for number in numbers:
    print(number)
    if number == 3:
        continue
    print('Next number should be ', number + 1) if number != 5 else print("loop's end") # for short hand conditions need both if and else statements
print('outside the loop')
# The range(start,stop, step) function is used to generate a sequence of numbers. The range function takes three arguments: start, stop, and step. The range function generates numbers starting from the start number, and stops before a specified number. The range function generates numbers by the step number. The default step number is 1.
lst = list(range(11)) 
print(lst) # [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
st = set(range(1, 11))    # 2 arguments indicate start and end of the sequence, step set to default 1
print(st) # {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}

lst = list(range(0,11,2))
print(lst) # [0, 2, 4, 6, 8, 10]
st = set(range(0,11,2))
print(st) #  {0, 2, 4, 6, 8, 10}
# range() in for loop example:
for number in range(11):
    print(number)   # prints 0 to 10, not including 11

# Nested for loops:
# syntax
# for x in y:
#     for t in x:
#         print(t)
person = {
    'first_name': 'Asabeneh',
    'last_name': 'Yetayeh',
    'age': 250,
    'country': 'Finland',
    'is_marred': True,
    'skills': ['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'address': {
        'street': 'Space street',
        'zipcode': '02210'
    }
}
for key in person:
    if key == 'skills':
        for skill in person['skills']:
            print(skill) # prints each skill in the list

# For Else: The else block will be executed when the loop ends and if the loop is not stopped by a break statement.
for number in range(11):
    print(number)   # prints 0 to 10, not including 11
else:
    print('The loop stops at', number) # prints 'The loop stops at 10'

# EXERCISES
for number in range(11):
    print(number)
# print 10 to 0 using for loop
for number in range(10, -1, -1):
    print(number);
# Use nested loops to create the following pattern
# # # # # # # # 
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
# # # # # # # #
for i in range(8): # Outer loop - runs 8 times (i goes from 0 to 7)
    for j in range(8): # Inner loop - runs 8 times (j goes from 0 to 7)
        print('#', end=' ') # print '#' and stay in the same line
    print() # print new line after finsihing inner loop
# Use for loop to iterate from 0 to 100 and print the sum of all numbers.
sum = 0
for number in range (101):
    sum += number
else:
    print('The sum of all numbers is', sum);
# import data from data/countries.py and write a for loop to print the countries
from data.countries import countries
for country in countries:
    if "land" in country:
        print(country)
# reverse this fruit list using for loop
fruits = ['banana', 'orange', 'mango', 'lemon']
reversed_fruits =[]
for i in range(len(fruits)-1, -1, -1):
    reversed_fruits.append(fruits[i]);
print(reversed_fruits)

# Look at data in data/countries-data.py and find:
# What are the total number of langauges spoken
language_set = set()
from data.countries_data import countries_data
for country in countries_data: # iterate over the list of countries
    for language in country['languages']: # iterate over the list of languages in each country
        language_set.add(language) # add the language to the set
print(language_set) # print the set to see the languages
print(len(language_set)) # print the length of the set to get the total number of languages
# 10 most spoken languages
from collections import Counter
popular_languages = {}
for country in countries_data:
    for language in country['languages']: # iterate over the list of languages in each country
        if language in popular_languages: # if the language is already in the dictionary
            popular_languages[language] += 1 # increment the count
        else: # if the language is not in the dictionary
            popular_languages[language] = 1  # add the language to the dictionary with a count of 1
popular_languages = dict(Counter(popular_languages).most_common(10)) # get the 10 most common languages using Counter
print(popular_languages) # print the 10 most common languages
# The 10 most populated countries
populations =dict()
for country in countries_data:
    populations[country['name']] = country['population'] # add the country name and population to the dictionary
populations = dict(Counter(populations).most_common(10)) # get the top 10 populatd couuntries
print(populations) # print the top 10 populated countries






