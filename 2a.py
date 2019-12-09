#!/usr/bin/python3

import sys

f = open(sys.argv[1], "r").read()

program = [int(x) for x in f.split(',')]
program[1] = 12
program[2] = 2

i = 0
last_result = 0

while i < len(program):
    if program[i] == 1:
        op_1 = program[i + 1]
        op_2 = program[i + 2]
        target = program[i + 3]
        last_result = program[target] = program[op_1] + program[op_2]
    elif program[i] == 2:
        op_1 = program[i + 1]
        op_2 = program[i + 2]
        target = program[i + 3]
        last_result = program[target] = program[op_1] * program[op_2]
    elif program[i] == 99:
        break
    i += 4

print(last_result)