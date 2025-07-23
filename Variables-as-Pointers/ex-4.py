'''Without running this code, what will it print? Why?'''


dict1 = {
    'a': [1, 2, 3],
    'b': (4, 5, 6),
}

dict2 = dict(dict1)
dict1['a'][1] = 42
print(dict2['a'])

'''It will print:

[1,42,3]

because dict2 object is referencing dict1 object, even 
though they are two seperate objects. So when dict1 object
is mutated, that reference is updated accordingly and dict2
is changed.

'''