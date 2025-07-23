'''Without running this code, what will it print? Why?'''


dict1 = {
    "Hitchhiker's Guide to the Galaxy": 42,
    'Monty Python': 'The Life of Brian',
    'Airplane!': "Don't call me Shirley!",
}

dict2 = dict(dict1)
dict2['Monty Python'] = 'Holy Grail'
print(dict1['Monty Python'])

'''It will print:

'The Life of Brian'

because the expression dict(dict1) created a new object, dict2. 
When the dictionary object, dict2 was mutated, it did not 
affect the dict1 dictionary object and so the key 
'Monty Python' pointed to its original value.

'''