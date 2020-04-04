#!/usr/bin/env python

def check_substrings(line):
    if(line.find('ab') != -1):
        return True
    if(line.find('cd') != -1):
        return True
    if(line.find('pq') != -1):
        return True
    if(line.find('xy') != -1):
        return True

def check_double(line):
    comp = ''
    for letter in line:
        if letter == comp:
            return False
        else:
            comp = letter

    return True

def check_vowels(line):
    a = 0
    e = 0
    i = 0
    o = 0
    u = 0
    
    for letter in line:
        if letter == 'a':
            a += 1
        elif letter == 'e':
            e += 1
        elif letter == 'i':
            i += 1
        elif letter == 'o':
            o += 1
        elif letter == 'u':
            u += 1

    if (a + e + i + o + u) >= 3:
        return False
    else:
        return True

nice = 0
    
with open('input') as file:
    for line in file:
        line = line.strip('\n')
        naughty = False
        naughty = naughty or check_substrings(line)
        naughty = naughty or check_double(line)
        naughty = naughty or check_vowels(line)

        if naughty:
            pass
        else:
            nice += 1
    
    
print(nice)
