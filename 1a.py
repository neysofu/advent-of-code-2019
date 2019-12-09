#!/usr/bin/python3

import sys


def calculate_fuel_for_module(n):
    return n // 3 - 2


f = open(sys.argv[1], "r").read()
total = 0
for line in f.splitlines():
    if line:
        total += calculate_fuel_for_module(int(line))

print(total)