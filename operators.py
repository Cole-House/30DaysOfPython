# print('== Addition, Subtraction, Multiplication, Division, Modulus ==')

# # Declaring values and organizing them together
# num_one = 3
# num_two = 4

# # Arithmetic operations
# total = num_one + num_two
# diff = num_two - num_one
# product = num_one * num_two
# div = num_two / num_one
# remainder = num_two % num_one

# # Printing values with label
# print('total: ', total)
# print('difference: ', diff)
# print('product: ', product)
# print('division: ', div)
# print('remainder: ', remainder)

# # Calculating area of a circle
# radius = 10                                 # radius of a circle
# area_of_circle = 3.14 * radius ** 2         # two * sign means exponent or power
# print('Area of a circle:', area_of_circle)

# # Calculating area of a rectangle
# length = 10
# width = 20
# area_of_rectangle = length * width
# print('Area of rectangle:', area_of_rectangle)

# # Calculating a weight of an object
# mass = 75
# gravity = 9.81
# weight = mass * gravity
# print(weight, 'N')                         # Adding unit to the weight

# # Calculate the density of a liquid
# mass = 75 # in Kg
# volume = 0.075 # in cubic meter
# density = mass / volume # 1000 Kg/m^3

# # Comparison Operators
# print(3 > 2)     # True, because 3 is greater than 2
# print(3 >= 2)    # True, because 3 is greater than 2
# print(3 < 2)     # False,  because 3 is greater than 2
# print(2 < 3)     # True, because 2 is less than 3
# print(2 <= 3)    # True, because 2 is less than 3
# print(3 == 2)    # False, because 3 is not equal to 2
# print(3 != 2)    # True, because 3 is not equal to 2
# print(len('mango') == len('avocado'))  # False
# print(len('mango') != len('avocado'))  # True
# print(len('mango') < len('avocado'))   # True
# print(len('milk') != len('meat'))      # False
# print(len('milk') == len('meat'))      # True
# print(len('tomato') == len('potato'))  # True
# print(len('python') > len('dragon'))   # False

# # Comparing something gives either a True or False

# print('True == True: ', True == True)
# print('True == False: ', True == False)
# print('False == False:', False == False)

# # In addition to above comparsion operators, python uses is, is not to compare objects and in and not in to check if an object exist in an object like list, tuple, set, string and dictionary.
# print('1 is 1', 1 is 1)                   # True - because the data values are the same
# print('1 is not 2', 1 is not 2)           # True - because 1 is not 2
# print('A in Asabeneh', 'A' in 'Asabeneh') # True - A found in the string
# print('B in Asabeneh', 'B' in 'Asabeneh') # False - there is no uppercase B
# print('coding' in 'coding for all') # True - because coding for all has the word coding
# print('a in an:', 'a' in 'an')      # True
# print('4 is 2 ** 2:', 4 is 2 ** 2)   # True

# Excercises Day 3 
age = 22;
height = 1.75;
comp = 3 + 4j;
# triangle_base = input('Enter the base of the triangle: ');
# triangle_height = input('Enter the height of the triangle: ');
# print('The area of the triangle is: ', 0.5 * int(triangle_base) * int(triangle_height));

print(len('python') != len('dragon')); # False
print(("on" in 'python') and ("on" in "dragon")); 
len_of_python = len('python');
len_to_float = float(len_of_python);
float_to_string = str(len_to_float);
print('The length of python is: ', len_of_python, ' and the length of python as a float is: ', len_to_float, ' and the float as a string is: ', float_to_string);
random_number = input('Enter a random number: ');
# print statement that tells if the inputted number is even or odd using the modulus operator
print('Was the number even?:  ', int(random_number) % 2 == 0); # True if even, False if odd
num = 1;
exp = 2;

# Loop through the numbers from 1 to 5 to print the values: n, 1, n^1, n^2, n^3.
for n in range(1, 6):
    print(f"{n} 1 {n} {n**2} {n**3}")




