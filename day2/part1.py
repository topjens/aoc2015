#!/usr/bin/env python

total = 0

with open('input') as input_file:
    for line in input_file:
        l, w, h = line.strip('\n').split('x')
        l = int(l)
        w = int(w)
        h = int(h)
        one = l * w
        two = l * h
        three = w * h
        slack = min(one, two, three)
        total += 2*one + 2*two + 2*three + slack

print(total)
