# -*- coding: utf-8 -*-
import sys


args = sys.argv
if len(args) == 2:
    num_lines = sum(1 for i in open(args[1]))
    print num_lines
