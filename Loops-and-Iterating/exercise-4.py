"""Use a while loop to print all numbers in my_list with even values, one number per 
line. Then, print the odd numbers using a ' for' loop."""

my_list = [6, 3, 0, 11, 20, 4, 17]

i = 0

while i < len(my_list):
    if my_list[i] % 2 == 0:
        print(my_list[i])

    i += 1

for i in range(len(my_list)):
    if my_list[i] % 2 != 0:
        print(my_list[i])