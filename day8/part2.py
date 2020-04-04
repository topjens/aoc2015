#!/usr/bin/env python

"""
Let's begin with a blank slate for day two.
"""

def encode(line):
    str = ''

    # Then loop over string and deal with character that have to be escaped
    for letter in line:
        if letter == '\\':
            str += '\\\\'
            continue
        if letter == '"':
            str += '\\"'
            continue
        str += letter

    return '"' + str + '"'

result = 0

with open('input') as file:
    for line in file:
        line = line.rstrip()
        result += len(encode(line)) - len(line)

print(result)
