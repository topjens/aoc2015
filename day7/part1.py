#!/usr/bin/env python

from collections import deque
import re
import numpy

assign = re.compile('([0-9]+) -> ([a-z]+)')
operation = re.compile('([a-z0-9]*) *([A-Z]+) ([a-z0-9]+) -> ([a-z]+)')

wires = {}

operation_queue = deque()

AND    = 1
NOT    = 2
OR     = 3
LSHIFT = 4
RSHIFT = 5

class Operation:
    def __init__(self, match):
        self.op1 = match.group(1)
        self.op2 = match.group(3)
        self.dest = match.group(4)
        
        if match.group(2) == 'AND':
            self.op = AND
        elif match.group(2) == 'NOT':
            self.op = NOT
            self.op1 = None
        elif match.group(2) == 'OR':
            self.op = OR
        elif match.group(2) == 'LSHIFT':
            self.op = LSHIFT
            self.op2 = int(self.op2)
        elif match.group(2) == 'RSHIFT':
            self.op = RSHIFT
            self.op2 = int(self.op2)
        else:
            raise Exception(f'Unknown operation {match.group(2)}')

    def __repr__(self):
        return f'{self.op1} {self.op} {self.op2} -> {self.dest}'

with open('test') as file:
    for line in file:
        match = assign.match(line)
        if(match):
            wires[match.group(2)] = int(match.group(1))
        else:
            match = operation.match(line)
            if(match):
                operation_queue.append(Operation(match))
            else:
                raise Exception(f'Syntax error: {line}')

while(operation_queue):
    op = operation_queue.popleft()
    if (op.op != NOT and op.op1 not in wires) or ((op.op != LSHIFT and op.op != RSHIFT) and op.op2 not in wires):
        operation_queue.append(op)
    else:
        if op.op == AND:
            wires[op.dest] = wires[op.op1] & wires[op.op2]
        elif op.op == OR:
            wires[op.dest] = wires[op.op1] | wires[op.op2]
        elif op.op == NOT:
            wires[op.dest] = ~ wires[op.op2]
        elif op.op == LSHIFT:
            wires[op.dest] = wires[op.op1] << op.op2
        elif op.op == RSHIFT:
            wires[op.dest] = wires[op.op1] >> op.op2

def int32_to_uint32(i):
    return numpy.uint16(numpy.int16(i))
            
for key, value in wires.items():
    print(key, int32_to_uint32(value))

