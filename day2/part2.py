#!/usr/bin/env python

import math

total = 0

with open('input') as input_file:
    for line in input_file:
        dimensions = []
        l, w, h = line.strip('\n').split('x')
        dimensions.append(int(l))
        dimensions.append(int(w))
        dimensions.append(int(h))
        ribbon = math.prod(dimensions)
        min1 = min(dimensions)
        dimensions.remove(min1)
        min2 = min(dimensions)
        total += 2 * min1 + 2 * min2 + ribbon

print(total)
