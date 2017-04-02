# -*- coding: utf-8 -*-
import sys


args = sys.argv
if len(args) == 3:
    col1 = []
    col2 = []
    mergeText = ''
    with open('col1.txt', 'r') as f:
        for row in f:
            col1.append(row)
    with open('col2.txt', 'r') as f:
        for row in f:
            col2.append(row)

    with open('merged.txt', 'w') as f:
        for (a, b) in zip(col1, col2):
            f.write(a[:-1] + '\t' + b)
