'''Building on your solutions from the previous exercises, 
write a function local_greet that takes a locale as input, 
and returns a greeting. The locale lets us greet people from 
different countries appropriately, even when they share a common
 language, for example:

Distinguish greetings for English speaking countries like the 
US, UK, Canada, or Australia in your implementation, and feel 
free to fall back on the language-specific greetings in all 
other cases.

When implementing local_greet, make sure you re-use your 
extract_language, extract_region, and greet functions from the 
previous exercises.
'''

def extract_lang_and_region(locale):
    return locale.split('.',)[0]

def extract_lang(string):
    return string[0:2]

def local_greet(locale):
    
    lang_and_region = extract_lang_and_region(locale)

    if "en" in lang_and_region:
        match lang_and_region:
            case 'en_US':
                return 'Hey!'
            case 'en_GB':
                return 'Hello!'
            case 'en_AU':
                return 'Howdy!'
    else:
        lang = extract_lang(lang_and_region)
        
        match lang:
            case 'fr':
                return 'Salut!'
            case 'pt':
                return 'Ola!'
            case 'de':
                return 'Hallo!'
            case 'sv':
                return 'Hej!'
            case 'af':
                return 'Haai!'

print(local_greet('en_US.UTF-8'))       # Hey!
print(local_greet('en_GB.UTF-8'))       # Hello!
print(local_greet('en_AU.UTF-8'))       # Howdy!
print(local_greet('fr_FR.UTF-8'))       # Salut!
print(local_greet('fr_CA.UTF-8'))       # Salut!
print(local_greet('fr_MA.UTF-8'))       # Salut!

