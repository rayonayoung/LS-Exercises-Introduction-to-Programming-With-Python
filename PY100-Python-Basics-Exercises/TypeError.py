'''The following code raises a TypeError:

tweet = 'Woohoo! :-)'

if len(tweet) > 140:
    print('Tweet is too long!')

length_of_tweet = len(tweet + 5)

What does a TypeError indicate? Try running the above 
code, then use the resulting error message to determine 
exactly what is wrong. (You don't have to fix this code.)'''

'''Answer:

A TypeError indicates that an operation or function was
appled to a value of the wrong type. 

In this case, the problem is that a string and an integer
cannot be concatenated.'''




