#!/usr/bin/env python

import hashlib

day_input = b'bgvyzdsv'

i = 0
while(True):
    i += 1
    out = hashlib.md5(day_input + str(i).encode()).hexdigest()[0:5]
    if out == '00000':
        break

print(i)
