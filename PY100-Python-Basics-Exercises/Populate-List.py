'''You want to add the numbers from 1 to 5 to a list, but the 
code below is not producing the expected result. How can you 
fix it?

numbers = []

for i in range(5):
    numbers.append(i)

print(numbers)
'''
#By default i will be 0-4. Need to change range.

numbers = []

for i in range(1,6):
    numbers.append(i)

print(numbers)


