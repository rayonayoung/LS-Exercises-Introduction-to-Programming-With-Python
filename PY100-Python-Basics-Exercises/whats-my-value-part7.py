'''What will the following code do and why? Don't run it until 
you have tried to answer.

a = 1

def my_function():
    global a
    a = 2

my_function()
print(a)
'''

'''Answer:
It will print a, which is 2. The global variable a was reassigned
within the function and the function was called. So the value of a
became 2 and that is what is printed.
'''