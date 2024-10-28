# multiline strings in python use triple quote
# multiline_string = '''I am a teacher and enjoy teaching.
# I didn't find anything as rewarding as empowering people.
# That is why I created 30 days of python.'''
# print(multiline_string)

# # String Concatenation
# first_name = 'Cole'
# last_name = 'House'
# space = ' '
# full_name = first_name  +  space + last_name
# print(full_name) # Asabeneh Yetayeh

# # Use of python escape characters
# print('I hope everyone is enjoying the Python Challenge.\nAre you ?') # line break
# print('Days\tTopics\tExercises') # adding tab space or 4 spaces 
# print('Day 1\t5\t5')
# print('Day 2\t6\t20')
# print('Day 3\t5\t23')
# print('Day 4\t1\t35')
# print('This is a backslash  symbol (\\)') # To write a backslash
# print('In every programming language it starts with \"Hello, World!\"') # to write a double quote inside a single quote
 
## Old style string formatting (% operator)
# %s - String (or any object with a string representation, like numbers)
# %d - Integers
# %f - Floating point numbers
# "%.number of digitsf" - Floating point numbers with fixed precision
# Strings only
# first_name = 'Asabeneh'
# last_name = 'Yetayeh'
# language = 'Python'
# formated_string = 'I am %s %s. I teach %s' %(first_name, last_name, language)
# print(formated_string)

# # Strings  and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formated_string = 'The area of circle with a radius %d is %.2f.' %(radius, area) # 2 refers the 2 significant digits after the point
# print(formated_string)

# python_libraries = ['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']
# formated_string = 'The following are python libraries:%s' % (python_libraries)
# print(formated_string) # "The following are python libraries:['Django', 'Flask', 'NumPy', 'Matplotlib','Pandas']"

# New style string formatting (str.format) introduced in Python 3
# format(): formats string into a nicer output
# first_name = 'Cole'
# last_name = 'House'
# language = 'Python'
# formated_string = 'I am {} {}. and I want to learn {}'.format(first_name, last_name, language)
# print(formated_string)
# a = 4
# b = 3

# print('{} + {} = {}'.format(a, b, a + b))
# print('{} - {} = {}'.format(a, b, a - b))
# print('{} * {} = {}'.format(a, b, a * b))
# print('{} / {} = {:.2f}'.format(a, b, a / b)) # limits it to two digits after decimal
# print('{} % {} = {}'.format(a, b, a % b))
# print('{} // {} = {}'.format(a, b, a // b))
# print('{} ** {} = {}'.format(a, b, a ** b))

# Strings  and numbers
# radius = 10
# pi = 3.14
# area = pi * radius ** 2
# formated_string = 'The area of a circle with a radius {} is {:.2f}.'.format(radius, area) # 2 digits after decimal
# print(formated_string)

# this is how string Interpolation/f-strings work in (Python 3.6+)
# a = 4
# b = 3
# print(f'{a} + {b} = {a +b}')
# print(f'{a} - {b} = {a - b}')
# print(f'{a} * {b} = {a * b}')
# print(f'{a} / {b} = {a / b:.2f}')
# print(f'{a} % {b} = {a % b}')
# print(f'{a} // {b} = {a // b}')
# print(f'{a} ** {b} = {a ** b}')

# Strings are sequence of characters
# language = 'Python'
# a,b,c,d,e,f = language # unpacking sequence characters into variables
# print(a) # P
# print(b) # y
# print(c) # t
# print(d) # h
# print(e) # o
# print(f) # n

# Slicing Python strings
# language = 'Python'
# first_three = language[0:3] # starts at zero index and up to 3 but not include 3
# print(first_three) #Pyt
# last_three = language[3:6]
# print(last_three) # hon
# # Another way
# last_three = language[-3:]
# print(last_three)   # hon
# last_three = language[3:]
# print(last_three)   # hon
# # reversing a string in python is so easy!
# greeting = 'Hello, World!'
# print(greeting[::-1]) # !dlroW ,olleH
# Skipping characterts while slicing
# language = 'Python'
# pto = language[0:6:2] #
# print(pto) # Pto

# STRING METHODS!!!
# challenge = 'thirty days of python'
# # capitalize(): Converts the first character of the string to capital letter
# print(challenge.capitalize()) # 'Thirty days of python'
# # count(): returns occurrences of substring in string, count(substring, start=.., end=..). The start is a starting indexing for counting and end is the last index to count.
# print(challenge.count('y')) # 3
# print(challenge.count('y', 7, 14)) # 1, 
# print(challenge.count('th')) # 2`
# # endswith(): Checks if a string ends with a specified ending
# print(challenge.endswith('on'))   # True
# print(challenge.endswith('tion')) # False
# # expandtabs(): Replaces tab character with spaces, default tab size is 8. It takes tab size argument
# print(challenge.expandtabs())   # 'thirty  days    of      python'
# print(challenge.expandtabs(10)) # 'thirty    days      of        python'
# # find(): Returns the index of the first occurrence of a substring, if not found returns -1
# print(challenge.find('y'))  # 5
# print(challenge.find('th')) # 0
# print(challenge.find('w')) # -1
# # rfind(): Returns the index of the last occurrence of a substring, if not found returns -1
# print(challenge.rfind('y'))  # 16
# print(challenge.rfind('th')) # 17
# # index(): Returns the lowest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1). If the substring is not found it raises a valueError.
# sub_string = 'da'
# print(challenge.index(sub_string))  # 7
# print(challenge.index(sub_string, 9)) # error
# # rindex(): Returns the highest index of a substring, additional arguments indicate starting and ending index (default 0 and string length - 1)
# print(challenge.rindex(sub_string))  # 7
# print(challenge.rindex(sub_string, 9)) # error
# print(challenge.rindex('on', 8)) # 19
# # isalnum(): checks if all characters in a string are alphanumeric
# challenge = '30DaysPython'
# print(challenge.isalnum()) # True
# challenge = 'thirty days of python'
# print(challenge.isalnum()) # False, space is not an alphanumeric character
# # isalpha(): Checks if all string elements are alphabet characters (a-z and A-Z)
# # isdecimal(): Checks if all characters in a string are decimal (0-9)
# # isdigit(): Checks if all characters in a string are numbers (0-9 and some other unicode characters for numbers)
# print(challenge.isdigit()) # False
# challenge = '30'
# print(challenge.isdigit())   # True
# challenge = '\u00B2'
# print(challenge.isdigit())   # True
# # isnumeric(): Checks if all characters in a string are numbers or number related (just like isdigit(), just accepts more symbols, like ½)
# num = '10'
# print(num.isnumeric()) # True
# num = '\u00BD' # ½
# print(num.isnumeric()) # True
# num = '10.5'
# print(num.isnumeric()) # False
# # isidentifier(): Checks for a valid identifier - it checks if a string is a valid variable name
# challenge = '30DaysOfPython'
# print(challenge.isidentifier()) # False, because it starts with a number
# challenge = 'thirty_days_of_python'
# print(challenge.isidentifier()) # True
# # islower(): Checks if all alphabet characters in the string are lowercase
# challenge = 'thirty days of python'
# print(challenge.islower()) # True
# challenge = 'Thirty days of python'
# print(challenge.islower()) # False
# # isupper(): Checks if all alphabet characters in the string are uppercase
# # join(): Returns a concatenated string
# web_tech = ['HTML', 'CSS', 'JavaScript', 'React']
# result = '# '.join(web_tech)
# print(result) # 'HTML# CSS# JavaScript# React'
# # strip(): Removes all given characters starting from the beginning and end of the string
# challenge = 'thirty days of pythoonnn'
# print(challenge.strip('noth')) # 'irty days of py'
# # replace(): Replaces substring with a given string
# challenge = 'thirty days of python'
# print(challenge.replace('python', 'coding')) # 'thirty days of coding'
# # split(): Splits the string, using given string or space as a separator
# print(challenge.split()) # ['thirty', 'days', 'of', 'python']
# challenge = 'thirty, days, of, python'
# print(challenge.split(', ')) # ['thirty', 'days', 'of', 'python']
# # title(): Returns a title cased string
# print(challenge.title()) # Thirty Days Of Python
# swapcase(): Converts all uppercase characters to lowercase and all lowercase characters to uppercase characters
# startswith(): Checks if String Starts with the Specified String







