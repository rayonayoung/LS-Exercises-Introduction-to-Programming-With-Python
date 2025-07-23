"""Write a function that computes and returns the factorial 
of a number by using a for or while loop. The factorial 
of a positive integer n, signified by n!, is defined as 
the product of all integers between 1 and n, inclusive:"""

def factorial(num):
    i = 1
    result = num
    while (i < num):
        
        result *= num - i
        i += 1

    return result

print(factorial(6))