'''Rewrite car as a list of lists in which each nested list 
contains two elements that represent the corresponding key/value 
pairs.

car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}'''
car = {
    'type':  'sedan',
    'color': 'blue',
    'year':  2003,
}
lst = []
pair = []

for key, value in car.items():
    lst.append([key,value])

print(lst)