#!/usr/bin/env python

with open('input') as input_file:
    input = input_file.read()

x = 0
y = 0
presents = {(x, y): 1}
    
for move in input:
    if move == '^':
        y += 1
    elif move == 'v':
        y -= 1
    elif move == '<':
        x -= 1
    elif move == '>':
        x += 1
    else:
        raise Exception(f'Unknown movement {move}')

    if (x,y) in presents:
        presents[(x,y)] += 1
    else:
        presents[(x,y)] = 1

print(len(presents))
