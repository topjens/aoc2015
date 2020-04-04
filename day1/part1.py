#!/usr/bin/env python

floor = 0

with open('input') as input_file:
    input = input_file.read()
    for par in input:
        if par == '(':
            floor += 1
        elif par == ')':
            floor -= 1
        else:
            raise Exception(f'Illegal character {par} in input!')

print(f'Santa has to be on floor {floor}')

    
