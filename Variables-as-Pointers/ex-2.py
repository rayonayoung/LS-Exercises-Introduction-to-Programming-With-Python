'''Without running this code, what will it print? Why?'''


set1 = {42, 'Monty Python', ('a', 'b', 'c')}
set2 = set1
set1.add(range(5, 10))
print(set2)

'''It will print:

set2 = {42, 'Monty Python', ('a', 'b', 'c'), range(5, 10)}

Because that is what set1 was mutated to and since set2 
is pointing to the same reference as set1, set2 was also
updated accordingly.
'''