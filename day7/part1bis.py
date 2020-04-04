#!/usr/bin/env python

from collections import deque
import re
import numpy

operation = re.compile('((?P<wire1>[a-z]+) ?|(?P<value1>[0-9]+) ?| ?)((?P<operation>[A-Z]+) | ?)((?P<wire2>[a-z]+) ?|(?P<value2>[0-9]+) ?| ?) -> (?P<dest>[a-z]+)')

wires = {}

operation_queue = deque()

AND    = 1
NOT    = 2
OR     = 3
LSHIFT = 4
RSHIFT = 5
ASSIGN = 6

WIRE = 1
VALUE = 2

class Operation:
    def __init__(self, match):
        if match.group('wire1'):
            self.src1 = match.group('wire1')
            self.src1_type = WIRE
        elif match.group('value1'):
            self.src1 = numpy.uint16(match.group('value1'))
            self.src1_type = VALUE
        else:
            self.src1 = None
            self.src1_type = None

        if match.group('wire2'):
            self.src2 = match.group('wire2')
            self.src2_type = WIRE
        elif match.group('value2'):
            self.src2 = numpy.uint16(match.group('value2'))
            self.src2_type = VALUE
        else:
            self.src2 = None
            self.src2_type = None
        
        if match.group('operation') == 'AND':
            self.op = AND
        elif match.group('operation') == 'NOT':
            self.op = NOT
            self.op1 = None
        elif match.group('operation') == 'OR':
            self.op = OR
        elif match.group('operation') == 'LSHIFT':
            self.op = LSHIFT
        elif match.group('operation') == 'RSHIFT':
            self.op = RSHIFT
        elif match.group('operation') == None:
            self.op = ASSIGN
        else:
            raise Exception(f'Unknown operation {match.group("operation")}')

        self.dest = match.group('dest')

    def __repr__(self):
        return f'{self.src1}[{self.src1_type}] {self.op} {self.src2}[{self.src2_type}] -> {self.dest}'

with open('input2') as file:
    for line in file:
        match = operation.match(line)
        if match:
            operation_queue.append(Operation(match))
        else:
            raise Exception(f'Syntax error {line}')

while(operation_queue):
    op = operation_queue.popleft()
    if (op.src1_type == WIRE and op.src1 not in wires) or (op.src2_type == WIRE and op.src2 not in wires):
        operation_queue.append(op)
    else:
        if op.src1_type == WIRE:
            op.src1 = wires[op.src1]
        if op.src2_type == WIRE:
            op.src2 = wires[op.src2]

        if op.op == AND:
            wires[op.dest] = op.src1 & op.src2
        elif op.op == OR:
            wires[op.dest] = op.src1 | op.src2
        elif op.op == NOT:
            wires[op.dest] = ~ op.src2
        elif op.op == LSHIFT:
            wires[op.dest] = op.src1 << op.src2
        elif op.op == RSHIFT:
            wires[op.dest] = op.src1 >> op.src2
        elif op.op == ASSIGN:
            wires[op.dest] = op.src1
        else:
            raise Exception(f'Unknown operation {op.op}')

print(wires)
print(wires['a'])
