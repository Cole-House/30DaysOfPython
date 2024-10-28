# Set is a collection of unordered and un-indexed distinct elements. In Python set is used to store unique items, and it is possible to find the union, intersection, difference, symmetric difference, subset, super set and disjoint set among sets.
# Creating a set
st = set();
st = {'item1', 'item2', 'item3', 'item4'}
# Checking an item in a set
print("Does set st contain item3? ", 'item3' in st) # Does set st contain item3? True
# Once a set is created we cannot change any items and we can also add additional items. using add() method
st.add('item5');
print(st);
# Add multiple items using update() The update() allows to add multiple items to a set. The update() takes a list argument.
fruits = {'banana', 'orange', 'mango', 'lemon'}
vegetables = ('tomato', 'potato', 'cabbage','onion', 'carrot')
fruits.update(vegetables)
print(fruits);
# We can remove an item from a set using remove() method. If the item is not found remove() method will raise errors, so it is good to check if the item exist in the given set. However, discard() method doesn't raise any errors.
fruits.remove('banana');
print(fruits);
# If we want to clear or empty the set we use clear() method.
fruits.clear();
# Converting a list to a set, and set to a list. Converting list to set removes duplicates and only unique items will be reserved.
lst = ['item1', 'item2', 'item3', 'item4', 'item1']
st = set(lst)  # {'item2', 'item4', 'item1', 'item3'} - the order is random, because sets in general are unordered
newLst = list(st) # ['item2', 'item4', 'item1', 'item3']
# Joining sets. We can join two sets using the union() or update() method.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st3 = st1.union(st2)
print(st3);
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item5', 'item6', 'item7', 'item8'}
st1.update(st2) # st2 contents are added to st1
print(st1);
# Finding intersection of two sets. The intersection() method returns a new set with items that are common in two sets.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item3', 'item2'}
st1.intersection(st2) # {'item3', 'item2'}
# Checking difference between two sets. The difference() method returns a new set with items in the set that are not in the other set.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
st2.difference(st1) # set()
st1.difference(st2) # {'item1', 'item4'} => st1\st2
# Checking subsewt and superset. The issubset() method returns True if all items in the set exists in the specified set, otherwise it retuns False. The issuperset() method returns True if all items in the specified set exists in the original set, otherwise it retuns False.
whole_numbers = {0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
even_numbers = {0, 2, 4, 6, 8, 10}
whole_numbers.issubset(even_numbers) # False, because it is a super set
whole_numbers.issuperset(even_numbers) # True
# Finding symmetric difference. The symmetric_difference() method returns a new set which contains items in both sets, but not the common ones.
st1 = {'item1', 'item2', 'item3', 'item4'}
st2 = {'item2', 'item3'}
# it means (A\B)∪(B\A)
st2.symmetric_difference(st1) # {'item1', 'item4'}
# Checking disjoint sets. Two sets are said to be disjoint if they have no common items. We can check if two sets are joint or disjoint using isdisjoint() method.
even_numbers = {0, 2, 4 ,6, 8}
odd_numbers = {1, 3, 5, 7, 9}
even_numbers.isdisjoint(odd_numbers) # True, because no common item
# Accessing items in a set requires using loops

# EXERCISES
it_companies = {'Facebook', 'Google', 'Microsoft', 'Apple', 'IBM', 'Oracle', 'Amazon'}
A = {19, 22, 24, 20, 25, 26}
B = {19, 22, 20, 25, 26, 24, 28, 27}
age = [22, 19, 24, 25, 26, 24, 25, 24]
# join A and B
C = A.union(B);
print(C);
# Find A intersection B
D = A.intersection(B);
print(D);
# Is A subset of B
print('Is A subset of B', A.issubset(B));
# Are A and B disjoint sets
print('Are A and B disjoint sets', A.isdisjoint(B));
# Join A with B and B with A
E = B.union(A);
print(E);
# What is the symmetric difference between A and B 
F = A.symmetric_difference(B);
print(F);
del A, B, C, D, E, F;
# Convert the ages to a set and compare the length of the list and the set, which one is bigger?
age_set = set(age);
print('Length of age list:', len(age));
print('Length of age set:', len(age_set));
# I am a teacher and I love to inspire and teach people. How many unique words have been used in the sentence? Use the split methods and set to get the unique words.
str = 'I am a teacher and I love to inspire and teach people';
# split the string into list of words
words = str.split();
# from list we can then change it to set to get unique words
unique_words = set(words);
print('Number of unique words:', len(unique_words));
