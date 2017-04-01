# -*- coding: utf-8 -*-
import sys


def createText(x, y, z):
    print x + "時の" + y + "は" + z


args = sys.argv


if len(args) == 4:
    x = args[1]
    y = args[2]
    z = args[3]
    createText(x, y, z)
