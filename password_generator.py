import pandas as pd
import random

print('Password Generator')

lower = 'abcdefghijklmnqrstuvwxyz'
lower = str(lower)
upper = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
upper = str(upper)
symbol = '!@$%^&*().,?'
symbol = str(symbol)
numeric = '0123456789'
numeric = str(numeric)

number = input('Number of passwords needed?')
number = int(number)

length = input('Password length?')
length = int(length)

min_lower = ing(input('Min lower case letters?'))
min_upper = int(input('Min upper case letters?'))
min_symbol = int(input('Min symbols?'))
min_num = int(input('Min Numbers?'))

char_count = min_lower+min_upper+min_symbol+min_number

print('\nHere are the passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(length):
        passwords += random.choice(lower)+random.choice(upper)+random.choice(symbol)+random.choice(numeric)
    print(passwords)

