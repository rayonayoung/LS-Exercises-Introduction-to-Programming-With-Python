'''We wanted to create a matrix 3x3 so we could use it to 
build a Tic-Tac-Toe game. However, we encountered an issue, as 
whenever we change a value in one nested list, 
all nested lists are affected. Can you fix the code?
sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list)

matrix[0][0] = "X"
print(matrix) # [['X', '-', '-'], ['X', '-', '-'], ['X', '-', '-']]
'''
import copy 
sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(copy.copy((sub_list)))

matrix[0][0] = "X"
print(matrix) 

