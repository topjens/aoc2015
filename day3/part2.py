#!/usr/bin/env python

with open('input') as input_file:
    input = input_file.read()

santa_x = 0
santa_y = 0
presents = {(santa_x, santa_y): 1}

robo_x = 0
robo_y = 0
presents = {(robo_x, robo_y): 2}
    
for i, move in enumerate(input):
    if(i % 2):
        if move == '^':
            santa_y += 1
        elif move == 'v':
            santa_y -= 1
        elif move == '<':
            santa_x -= 1
        elif move == '>':
            santa_x += 1
        else:
            raise Exception(f'Unknown movement {move}')

        if (santa_x,santa_y) in presents:
            presents[(santa_x,santa_y)] += 1
        else:
            presents[(santa_x,santa_y)] = 1
    else:
        if move == '^':
            robo_y += 1
        elif move == 'v':
            robo_y -= 1
        elif move == '<':
            robo_x -= 1
        elif move == '>':
            robo_x += 1
        else:
            raise Exception(f'Unknown movement {move}')

        if (robo_x,robo_y) in presents:
            presents[(robo_x,robo_y)] += 1
        else:
            presents[(robo_x,robo_y)] = 1

print(len(presents))
