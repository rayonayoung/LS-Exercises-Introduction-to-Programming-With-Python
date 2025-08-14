'''We generated parts of a passcode and now want to combine 
them into a string. Write some code that creates and prints a 
string that contains each portion of the passcode separated by 
hyphens (-).

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

# Expected output: 11-jZ5-hQ3f*-8!7g3-p3Fs
'''
passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

output = '-'.join(passcode)

print(output)

