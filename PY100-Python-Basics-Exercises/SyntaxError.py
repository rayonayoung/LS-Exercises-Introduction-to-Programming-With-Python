'''The following code raises a SyntaxError:

speed_limit = 60
current_speed = 80

if current_speed > speed_limit
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')

What does a SyntaxError indicate? Try running the above 
code, then use the resulting error message to fix the 
error.      
'''

'''Answer:
SyntaxError indicates the code has not been formatted
correctly according to the standards of the Python language.'''
#Corrected
speed_limit = 60
current_speed = 80

if current_speed > speed_limit:
    print('"People are so bad at driving cars that '
          "computers don\'t have to be that good to be "
          'much better." -- Marc Andreessen')

