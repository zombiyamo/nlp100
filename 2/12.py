# -*- coding: utf-8 -*-
import sys


args = sys.argv
if len(args) == 2:
    col1 = []
    col2 = []
    for line in open(args[1]):
        lines = line.split()
        col1.append(lines[0])
        col2.append(lines[1])

    with open('col1.txt', 'w') as f:
        for col in col1:
            f.write(col + '\n')
    with open('col2.txt', 'w') as f:
        for col in col2:
            f.write(col + '\n')
