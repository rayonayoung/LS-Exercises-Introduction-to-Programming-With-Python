'''Write a function that checks whether a string starts 
with a specific prefix.

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True
'''

def starts_with(string, prefix):
    return string[0:len(prefix)].lower() == prefix.lower()

print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True

#Alternate:

def alt_starts_with(string, prefix):
    return string.startswith(prefix)

print(alt_starts_with("launch", "la"))   # True
print(alt_starts_with("school", "sah"))  # False
print(alt_starts_with("school", "sch"))  # True
