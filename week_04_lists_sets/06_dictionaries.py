# Author: Rusiru Fernando
# Dictionary: Collection of key-value pairs
# Properties:
#   unordered
#   mutable (i.e. can be changed) - can add, remove, update elements
#   no indexing
#   no duplicate keys allowed
#   duplicate values are allowed
#   keys are unique
#   values are not unique
#   keys are immutable (i.e. cannot be changed)
#   values are mutable (i.e. can be changed)
#   keys are case sensitive

# format: dictionary_name = {key1: value1, key2: value2, key3: value3, ...} - PEP8 recommends to use single quotes, space after comma
# key-value pairs are separated by comma


# dictionary with multiple key-value pairs
dict_03 = {'name': 'John', 'age': 25, 'address': 'Colombo'}
print(dict_03)

# dictionary with duplicate keys
dict_04 = {'name': 'John', 'age': 25, 'address': 'Colombo', 'name': 'Ellie'}  # duplicate keys are not allowed. prints only the last key-value pair
print(dict_04)

# indexing in dictionary
# print(dict_03[0])  # error - no indexing in dictionary
print(dict_03['name'])

# update dictionary
dict_03['name'] = 'Ellie'
print(dict_03)

# get() method - returns the value of the specified key
print(dict_03.get('name'))

# keys() method - returns a list containing the dictionary's keys
print(dict_03.keys())

# values() method - returns a list of all the values in the dictionary
print(dict_03.values())

# items() method - returns a list containing a tuple for each key value pair
print(dict_03.items())

# pop() method - removes the element with the specified key
dict_03.pop('name')
print(dict_03)

# popitem() method - removes the last inserted key-value pair
dict_03.popitem()
print(dict_03)

# clear() method - empties the dictionary
dict_03.clear()
print(dict_03)

# del keyword - deletes the dictionary completely
del dict_03
# print(dict_03)  # error - name 'dict_03' is not defined

# nested dictionary
dict_05 = {'name': 'John', 'age': 25, 'address': {'city': 'Colombo', 'country': 'Sri Lanka'}, 3: [1, 2, 3, 4, 5]}
print(dict_05)

# nested dictionary - access elements
print(dict_05['address']['city'])
print(dict_05[3][2])

# nested dictionary - update elements
dict_05['address']['city'] = 'Kandy'
print(dict_05)

# nested dictionary - add elements
dict_05['address']['zip_code'] = 20000
print(dict_05)

# nested dictionary - delete elements
del dict_05['address']['zip_code']
print(dict_05)

# nested dictionary - delete elements
del dict_05[3][2]
print(dict_05)

# len() method - returns the number of key-value pairs in the dictionary
print(len(dict_05))

# copy() method - returns a copy of the dictionary
dict_06 = dict_05.copy()
print(dict_06)

# dict() method - returns a dictionary
dict_07 = dict(name='John', age=25, address='Colombo')
print(dict_07)

# fromkeys() method - returns a dictionary with the specified keys and values
dict_08 = dict.fromkeys(['name', 'age', 'address'], 'unknown')

dict_08 = dict.fromkeys(['name', 'age', 'address'], ['unknown', 'unknown', 'unknown'])  # values can be a list
print(dict_08)

dict_08 = dict.fromkeys(['name', 'age', 'address'], ('unknown', 'unknown', 'unknown'))  # values can be a tuple
print(dict_08)

dict_08 = dict.fromkeys(['name', 'age', 'address'], {'name': 'unknown', 'age': 'unknown', 'address': 'unknown'})  # values can be a dictionary
print(dict_08)

# update() method - updates the dictionary with the specified key-value pairs
dict_09 = {'name': 'John', 'age': 25, 'address': 'Colombo'}
dict_10 = {'name': 'Ellie', 'age': 30, 'address': 'Kandy'}
dict_09.update(dict_10)
print(dict_09)

# setdefault() method - returns the value of the specified key. if the key does not exist, insert the key, with the specified value
dict_11 = {'name': 'John', 'age': 25, 'address': 'Colombo'}
print(dict_11.setdefault('name'))
print(dict_11.setdefault('dob', '1995-01-01'))
print(dict_11)