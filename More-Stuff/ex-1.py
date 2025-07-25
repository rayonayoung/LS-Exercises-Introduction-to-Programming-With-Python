'''What does the following function do? Be sure to 
identify the output value.'''

def do_something(dictionary):
    return sorted(dictionary.keys())[1].upper()

my_dict = {
    'Karl':     108,
    'Clare':    175,
    'Karis':    140,
    'Trevor':   180,
    'Antonina': 132,
    'Chris':    101,
}

print(do_something(my_dict))

'''It will sort the keys of the dictionary by alphabetical
order A-Z, then it will return the value of the newly sorted
index 1, capitalized.

In the case of my_dict, that value will be CHRIS.'''
