'''Determine what the following code snippet prints. 
First solve it in your head or on paper, then run it in 
your Python environment to check the result.

speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and 
(speed > 0 or acceleration > 0)
print(is_moving)
'''
'''Output will be True.
braking_force < acceleration = True
(speed > 0 or acceleration > 0) = True

True and  True = True
'''
speed = 0
acceleration = 24
braking_force = 19
is_moving = braking_force < acceleration and (speed > 0 or acceleration > 0)
print(is_moving)

'''Bonus question: Do we need the parentheses in the 
boolean expression or could we have written the 
following?:
is_moving = braking_force < acceleration and 
speed > 0 or acceleration > 0
'''

'''Answer:
braking_force < acceleration = True
speed > 0 = False
acceleration > 0 = True

True and False or True = True

The output would have been the same'''


