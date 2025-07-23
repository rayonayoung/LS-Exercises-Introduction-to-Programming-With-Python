"""Write a find_integers function that returns a list of
 all the integers from my_tuple"""

my_tuple = (1, 'a', '1', 3, [7], 3.1415,
            -4, None, {1, 2, 3}, False)

def find_integers(tuple):

    result_list = []
    
    for i in tuple:
        if type(i) is int:
            result_list.append(i)
    return result_list

print(find_integers(my_tuple))



