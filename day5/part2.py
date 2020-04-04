#!/usr/bin/env python

def check_double(line):
    for i in range(len(line) - 1):
        str1 = line[i:i+2]
        for j in range(len(line) - 1):
            if (j == i - 1) or (j == i) or (j == i + 1):
                continue
            str2 = line[j:j+2]
            if str1 == str2:
                return False

    return True

def check_repeat(line):
    first = ''
    second = ''

    for letter in line:
        if letter == first:
            return False
        else:
            first = second
            second = letter

    return True

nice = 0
    
with open('input') as file:
    for line in file:
        naughty = False
        naughty = naughty or check_double(line)
        naughty = naughty or check_repeat(line)
    
        if naughty:
            pass
        else:
            nice += 1
    
print(nice)

"""
lines = ['qjhvhtzxzqqjkmpb', 'xxyxx', 'uurcxstgmygtbstg', 'ieodomkazucvgmuy']
        
for line in lines:
    naughty = False
    naughty = naughty or check_double(line)
    naughty = naughty or check_repeat(line)

    if(naughty):
        print(f'{line} is naughty!')
    else:
        print(f'{line} is nice!')
"""



