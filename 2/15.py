# -*- coding: utf-8 -*-
import sys

args = sys.argv

if len(args) == 3:
    num_lines = sum(1 for i in open(args[1]))

    for i, line in enumerate(open(args[1])):
        if i >= num_lines - int(args[2]):
            print line
