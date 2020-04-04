#!/usr/bin/env python

"""
The implementation in this file is rather naive, scanning over every string
letter by letter. It would probably be better to just substitute substrings.
"""

ascii_table = [
    '0x00', '0x01', '0x02', '0x03', '0x04', '0x05', '0x06', '0x07', '0x08', '\t', '\n', '0x0B', '0x0C', '0x0D', '0x0E', '0x0F', '0x10', '0x11', '0x12', '0x13', '0x14', '0x15', '0x16', '0x17', '0x18', '0x19', '0x1A', '0x1B', '0x1C', '0x1D', '0x1E', '0x1F', ' ', '!', '"', '#', '$', '%', '&', '\'', '(', ')', '*', '+', ',', '-', '.', '/', '0', '1', '2', '3', '4', '5', '6', '7', '8', '9', ':', ';', '<', '=', '>', '?', '@', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', '[', '\\', ']', '^', '_', '`', 'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', '{', '|', '}', '~', 'ESC', 
] + [' '] * 128


"""
This funtion returns the string, complete with lookup into the ascii table
above. It is not suited to answer our question, because some ascii codes are
displayed as 0 or 2+ characters, as illustrated in the main program.
"""
def build_string(line):
    escape = False
    ascii = False
    ascii2 = False
    str = ''
    for letter in line:
        if escape:
            if letter == 'x':
                escape = False
                ascii = True
                code = 0
                continue
            if letter == '\\':
                escape = False
                str += '\\'
                continue
            if letter == '"':
                escape = False
                str += '"'
                continue
        if letter == '\\':
            escape = True
            continue
        if ascii:
            code += int(letter, 16)*16
            ascii = False
            ascii2 = True
            continue
        if ascii2:
            code += int(letter, 16)
            str += ascii_table[code]
            ascii2 = False
            continue
            
        if letter == '"':
            continue
        
        str += letter

    return str

"""
This funtion returns the length of the string, taking care in counting every
ascii code as 1 character.
"""
def line_length(line):
    length = 0
    escape = False
    ascii = False
    ascii2 = False
    for letter in line:
        if escape:
            if letter == 'x':
                escape = False
                ascii = True
                continue
            if letter == '\\':
                escape = False
                length += 1
                continue
            if letter == '"':
                escape = False
                length += 1
                continue
        if letter == '\\':
            escape = True
            continue
        if ascii:
            ascii = False
            ascii2 = True
            continue
        if ascii2:
            length += 1
            ascii2 = False
            continue
            
        if letter == '"':
            continue
        
        length += 1

    return length
            
result = result2 = 0

with open('input') as file:
    for line in file:
        line = line.rstrip()
        #print(len(line), line, len(build_string(line)), build_string(line))
        result += len(line) - len(build_string(line))
        result2 += len(line) - line_length(line)

"""
result2 will contain the answer to day 8 part 1. result is used to demonstrate
why build_string will not yield the right anwser
"""
print(result, result2)
