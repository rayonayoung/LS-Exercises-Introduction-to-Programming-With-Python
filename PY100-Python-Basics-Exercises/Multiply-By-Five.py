'''When the user inputs 10, we expect the program to print 
The result is 50!, but that's not the output we see. Why not?

def multiply_by_five(n):
    return n * 5

print("Hello! Which number would you like to multiply by 5?")
number = input()

print(f"The result is {multiply_by_five(number)}!")
'''
'''Answer: Because input() returns a string by default so the
output would be 1010101010. We could fix by changing to:

number = int(input())
'''

