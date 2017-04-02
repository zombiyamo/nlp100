# -*- coding: utf-8 -*-
import sys


args = sys.argv
if len(args) == 2:
    for line in open(args[1]):
        print line.replace('\t', '    ')
