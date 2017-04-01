# -*- coding: utf-8 -*-
import sys
import random


def typoglycemia(text):
    for i in range(len(text)):
        if len(text[i]) > 4:
            rand = range(1, len(text[i])-1)
            random.shuffle(rand)
            randText = ''
            for j in rand:
                randText += text[i][j]
            text[i] = text[i][0] + randText + text[i][-1]

    return " ".join(text)


args = sys.argv
text = ''
if len(args) >= 2:
    for i in xrange(len(args)-1):
        text += args[i+1] + ' '
    text = text.split()
    print typoglycemia(text)
