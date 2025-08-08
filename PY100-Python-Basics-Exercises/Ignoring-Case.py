'''Using the following code, compare the value of name with the 
string 'RoGeR' while ignoring the case of both strings. Print 
true if the values are the same; print false if they aren't. 
Next, perform a case-insensitive comparison between the value of
 name and the string 'DAVE'.

 name = 'Roger'
'''
name = 'Roger'
test_string = 'RoGeR'

if name.casefold() == test_string.casefold():
    print('True')
else:
    print('False')

test_string2 = 'DAVE'

if name.casefold() == test_string2.casefold():
    print('True')
else:
    print('False')