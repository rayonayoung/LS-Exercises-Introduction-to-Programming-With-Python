'''Write code that capitalizes the words in the string 
'launch school tech & talk', so that you get the string 
'Launch School Tech & Talk'.
'''
string = 'launch school tech & talk'
words = string.split()

i = 0
capitalized_list = []

for i in range(len(words)):
    new_word = words[i][0].upper() + words[i][1::] 
    capitalized_list.append(new_word)

capitalized_string = " ".join(capitalized_list)
print(capitalized_string)