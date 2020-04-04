#!/usr/bin/env python

import re

regex = re.compile('([a-z ]+) ([0-9]+,[0-9]+) ([a-z ]+) ([0-9]+,[0-9]+)')

lights = {}

for x in range(1000):
    for y in range(1000):
        lights[(x,y)] = False

with open('input') as file:
    for line in file:
        match = regex.match(line)
        xinit, yinit = match.group(2).split(',')
        xfin, yfin = match.group(4).split(',')
        xinit = int(xinit)
        yinit = int(yinit)
        xfin = int(xfin)
        yfin = int(yfin)

        if match.group(1) == 'turn on':
            for x in range(xinit, xfin + 1):
                for y in range(yinit, yfin + 1):
                    lights[(x,y)] = True
        elif match.group(1) == 'turn off':
            for x in range(xinit, xfin + 1):
                for y in range(yinit, yfin + 1):
                    lights[(x,y)] = False
        elif match.group(1) == 'toggle':
            for x in range(xinit, xfin + 1):
                for y in range(yinit, yfin + 1):
                    lights[(x,y)] = not lights[(x,y)]

count = 0
                    
for x in range(1000):
    for y in range(1000):
        if lights[(x,y)]:
            count += 1

print(count)
                
                    
