'''Write a function that returns the last element of a list 
provided as an argument. For example:

print(last(['Earth', 'Moon', 'Mars']))  # Mars

Be sure to handle the case where the input list is empty'''

def last(lst):
    if len(lst) > 0:
        return lst[len(lst)-1]
    else:
        return None

print(last(['Earth', 'Moon', 'Mars']))  # Mars
print(last([])) #None