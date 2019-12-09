#!/usr/bin/python3

import sys


def calculate_fuel_for_module(n):
    total = 0
    while True:
        n = n // 3 - 2
        if n <= 0:
            break
        total += n
    return total


f = open(sys.argv[1], "r").read()
total = 0
for line in f.splitlines():
    if line:
        total += calculate_fuel_for_module(int(line))

print(total)