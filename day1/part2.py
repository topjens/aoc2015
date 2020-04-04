#!/usr/bin/env python

floor = 0

with open('input') as input_file:
    input = input_file.read()
    for i, par in enumerate(input):
        if par == '(':
            floor += 1
        elif par == ')':
            floor -= 1
            if(floor < 0):
                print(f'The first time santa goes to the basement is {i+1}')
                break
        else:
            raise Exception(f'Illegal character {par} in input!')
