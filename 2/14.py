# -*- coding: utf-8 -*-
import sys

args = sys.argv

if len(args) == 3:
    for i, line in enumerate(open(args[1])):
        if i <= int(args[2]):
            print line
