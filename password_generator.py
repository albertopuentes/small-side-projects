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
options = lower+upper+symbol+numeric

number = input('Number of passwords needed?')
number = int(number)

length = input('Password length?')
length = int(length)

min_lower = int(input('Min lower case letters?'))
min_upper = int(input('Min upper case letters?'))
min_symbol = int(input('Min symbols?'))
min_num = int(input('Min Numbers?'))

char_count = min_lower+min_upper+min_symbol+min_num

print('\nHere are the passwords:')

for pwd in range(number):
    passwords = ''
    for c in range(min_lower):
        passwords += random.choice(lower)
    for c in range(min_upper):
        passwords += random.choice(upper)
    for c in range(min_symbol):
        passwords += random.choice(symbol)
    for c in range(min_num):
        passwords += random.choice(numeric)

    if char_count < length:
        for i in range(length - char_count):
            passwords += random.choice(options)
        print(passwords)



