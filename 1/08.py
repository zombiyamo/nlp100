# -*- coding: utf-8 -*-
import sys


def cipher(text):
    rText = ''
    for letter in text:
        if 97 <= ord(letter) <= 122:
            rText += chr(219 - ord(letter))
        else:
            rText += letter
    return rText
    # return "".join(chr(219-ord(c)) if c.islower() else c for in text)


args = sys.argv
text = ''
if len(args) >= 2:
    for i in xrange(len(args)-1):
        text += args[i+1] + ' '
    print cipher(text)
    print cipher(cipher(text))
