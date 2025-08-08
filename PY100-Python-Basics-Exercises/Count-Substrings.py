'''Write a function that counts the number of occurrences 
of a substring in a string.

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0
'''

def count_substrings(string, sub_string):
    return len(string.split(sub_string)) - 1

print(count_substrings("lemon lemon lemon", "lemon")) # 3
print(count_substrings("laLAlaLA", "la")) # 2
print(count_substrings("launch", "uno")) # 0

'''Alternate
def count_substrings(string, substring):
    return string.count(substring)'''