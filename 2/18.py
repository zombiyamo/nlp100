# -*- coding: utf-8 -*-
import sys
from prettyprint import pp
from operator import itemgetter

args = sys.argv
lineList = []
if len(args) == 2:
    for line in open(args[1]):
        lineList.append(line.split())
    lineList.sort(key=itemgetter(2))
    lineList.reverse
    pp(lineList)
