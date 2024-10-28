# Creating a tuple
empty_tuple = ()
# or using the tuple constructor
empty_tuple = tuple()
# use len() to check the number of items in a tuple
fruits = ('banana', 'orange', 'mango', 'lemon')
print(len(fruits));
# Accessing tuple items by index is similar to lists
first_fruit = fruits[0]
print(first_fruit);
# We can slice out a sub-tuple by specifying a range of indexes where to start and where to end in the tuple, the return value will be a new tuple with the specified items.
tpl = ('item1', 'item2', 'item3','item4')
all_items = tpl[0:4]         # all items
all_items = tpl[0:]         # all items
middle_two_items = tpl[1:3]  # does not include item at index 3
# Checking if an item exists in the tuple; using the in keyword
fruits = ('banana', 'orange', 'mango', 'lemon')
print('orange' in fruits) # True
print('apple' in fruits) # False
# fruits[0] = 'apple' # TypeError: 'tuple' object does not support item assignment
# Joining tuples
tpl1 = ('item1', 'item2', 'item3')
tpl2 = ('item4', 'item5','item6')
tpl3 = tpl1 + tpl2
print(tpl3);
#  It is not possible to remove a single item in a tuple but it is possible to delete the tuple itself using del.
tpl1 = ('item1', 'item2', 'item3')
del tpl1

# EXERCISES
# Create fruits, vegetables and animal products tuples. Join the three tuples and assign it to a variable called food_stuff_tp.
fruits = ('banana', 'orange', 'mango', 'lemon');
vegetables = ('potato', 'onion', 'carrot');
animal_products = ('meat', 'milk', 'butter');
food_stuff_tp = fruits + vegetables + animal_products;
print(food_stuff_tp);
# Change the about food_stuff_tp tuple to a food_stuff_lt list
food_stuff_lt = list(food_stuff_tp);
print(food_stuff_lt); 
