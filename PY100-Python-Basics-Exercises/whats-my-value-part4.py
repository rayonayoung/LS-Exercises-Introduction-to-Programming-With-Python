'''What will the following code do and why? Don't run it until 
you have tried to answer.

a = 1

def my_function():
    print(a)

my_function()
'''

'''Answer:
It will print a, which is 1.

This is different from the previous example because the function
only reads the global variable a because a had not
been assigned locally.  But in the previous example, x
was assigned within the function and that became the local
variable.  Since that local variable had not been given
a value, having x = x + 5 did not work because the x on the right
side of the assignment had not been defined.
'''