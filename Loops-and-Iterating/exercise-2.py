"""age.py: Write a program named age.py that asks the user 
to enter their age, then calculates and reports the 
future age 10, 20, 30, and 40 years from now.

Modify the age.py program you wrote in Exercise 3 of the 
Input/Output chapter. The updated code should use a for 
loop to display the future ages."""

def age():
    age = int(input('How old are you? '))
    step = 0
    num_years = 0

    print(f'You are {age} years old.')

    for i in range(4):
        i += 1
        step = 10
        num_years += step
        age += step
        print(f'In {num_years} years, you will be {age} years old. ')

age()