# -*- coding: utf-8 -*-
import sys
from prettyprint import pp

args = sys.argv
wordList = []
if len(args) == 2:
    for line in open(args[1]):
        lines = line.split()
        if lines[0] not in wordList:
            wordList.append(lines[0])
    pp(wordList)
