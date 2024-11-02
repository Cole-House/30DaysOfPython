# If condition is used to check if a condition is true or false. If the condition is true, the code inside the if block will be executed. If the condition is false, the code inside the if block will not be executed. The syntax of the if statement is as follows:
# syntax
# if condition:
#     this part of code runs for truthy conditions
a = 3
if a > 0:
    print('A is a positive number')
# A is a positive number
# If else statement example:
a = 3
if a < 0:
    print('A is a negative number')
else:
    print('A is a positive number')
# A is a positive number
# If elif (else if) else statements are used to check multiple conditions.
a = 0
if a > 0:
    print('A is a positive number')
elif a < 0:
    print('A is a negative number')
else:
    print('A is zero')
# A is zero
# Short hand if statement syntax:
# syntax
# code if condition else code
a = 3
print('A is positive') if a > 0 else print('A is negative') # first condition met, 'A is positive' will be printed
# There can also be nested if statements
# syntax
# if condition:
#     code
#     if condition:
#     code

# We can also use logical operators to combine conditional statements
# and: Returns True if both statements are true
# syntax
# if condition and condition:
#     code
a = 0
if a > 0 and a % 2 == 0:
        print('A is an even and positive integer')
elif a > 0 and a % 2 !=  0:
     print('A is a positive integer')
elif a == 0:
    print('A is zero')
else:
    print('A is negative')
# or: Returns True if one of the statements is true
# syntax
# if condition or condition:
#     code
user = 'James'
access_level = 3
if user == 'admin' or access_level >= 4:
        print('Access granted!')
else:
    print('Access denied!')

# EXERCISES
# Get user input using input(“Enter your age: ”). If user is 18 or older, give feedback: You are old enough to drive. If below 18 give feedback to wait for the missing amount of years.
age = int(input('Enter your age:'))
if age >= 18:
    print('You are old enough to drive')
else: 
    print(f'You will need to wait {18 - age } years to drive')

score = 45
if score >= 80 and score <= 100:
     print('A');
elif score >= 70 and score < 80:
    print('B')
elif score >= 60 and score < 70:
    print('C')
elif score >= 50 and score < 60:
    print('D')
elif score >= 45 and score < 50:
    print('F')

fruits = ['banana', 'orange', 'mango', 'lemon']
new_fruit = input('Enter a fruit:')
if new_fruit in fruits:
    print('That fruit already exists in the list')
else:
    fruits.append(new_fruit)
    print(fruits)