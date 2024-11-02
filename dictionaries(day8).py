# A dictionary is a collection of unordered, modifiable(mutable) paired (key: value) data type.
# syntax
empty_dict = {}
# Dictionary with data values
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
print(person)
# The dictionary above shows that a value could be any data types:string, boolean, list, tuple, set or a dictionary.
# Dictionary length checks the number of 'key: value' pairs in the dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(len(dct)) # 4
# Accessing dictionary items by referring to its key name inside square brackets
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
print(person['first_name']) # Asabeneh
print(person['country'])    # Finland
print(person['skills'])     # ['JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person['skills'][0])  # JavaScript
print(person['address']['street']) # Space street
# print(person['city'])       # Error
#  To avoid the error we can use the get() method, which will return None if the key does not exist
print(person.get('first_name')) # Asabeneh
print(person.get('country'))    # Finland
print(person.get('skills')) #['HTML','CSS','JavaScript', 'React', 'Node', 'MongoDB', 'Python']
print(person.get('city'))   # None
# Adding items to a dictionary is done by using adding a new key:item pair
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
person['job_title'] = 'Instructor'
person['skills'].append('HTML')
print(person)
# Modifying a value in a dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct['key1'] = 'value-one'
# Checking if a key exists in a dictionary, using the in keyword
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print('key2' in dct) # True
print('key5' in dct) # False
# Removing Key and Value Pairs from a Dictionary; pop(key): removes the item with the specified key name:,popitem(): removes the last item, del: removes an item with specified key name
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
person.pop('first_name')        # Removes the firstname item
person.popitem()                # Removes the address item
# del person['is_married']        # Removes the is_married item
# Changing Dictionary to a List of Items
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.items()) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4')])
# Clearing all items out of a Dictionary we use the clear() method
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
print(dct.clear()) # None
# Deleting a Dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
del dct
# Copying a Dictionary using the copy() method; avoids mutation of original dictionary
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
dct_copy = dct.copy() # {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
#  Getting all keys from a dictionary using the keys() method
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
keys = dct.keys()
print(keys)     # dict_keys(['key1', 'key2', 'key3', 'key4'])
#  also can get all values from a dictionary using the values() method
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
values = dct.values()
print(values)     # dict_values(['value1', 'value2', 'value3', 'value4'])
# Getting all key:value pairs from a dictionary using the items() method
dct = {'key1':'value1', 'key2':'value2', 'key3':'value3', 'key4':'value4'}
items = dct.items()
print(items) # dict_items([('key1', 'value1'), ('key2', 'value2'), ('key3', 'value3'), ('key4', 'value4'])  

# EXCERCISES
dog = {
    'name': 'Monty',
    'color': 'White',
    'breed': 'Tibetan spaniel',
    'legs': 4,
}
dog['age'] = 10;
student = {
    'first_name':'Cole',
    'last_name':'House',
    'age':22,
    'country':'Drainlandia',
    'is_marred':True,
    'skills':['JavaScript', 'React', 'Node', 'MongoDB', 'Python'],
    'city':'Drain city',
    'address':{
        'street':'Space street',
        'zipcode':'02210'
        }
}
print(len(student));
# Get the value of skills and check the data type, it should be a list
print(type(student.get('skills')));
# Modify the skills values by adding one or two skills
student['skills'].append('Next.JS');
# Change the disctionary to a lost of tuples using the items() method
# you use the list() function to convert the dict_items view into an actual list. This makes the data more accessible for operations where a list structure is beneficial
print(list(student.items()));
