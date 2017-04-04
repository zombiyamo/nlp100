# -*- coding: utf-8 -*-
import sys
from operator import itemgetter
from prettyprint import pp

args = sys.argv
lineList = []
sortedfreq = []
if len(args) == 2:
    for line in open(args[1]):
        lineList.append(line.split())
    for i, key in enumerate(set(map(itemgetter(0), lineList))):
        sortedfreq.append([key, map(itemgetter(0), lineList).count(key)])
    sortedfreq.sort(key=itemgetter(1))
    sortedfreq.reverse()
    for word in map(itemgetter(0), sortedfreq):
        for line in lineList:
            if word in line:
                pp(line)
