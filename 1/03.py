# -*- coding: utf-8 -*-
import string

str = "Now I need a drink, alcoholic of course, after the heavy lectures involving quantum mechanics.".translate(None,',.')
strlength = []
strs = str.split()
for i in strs:
	strlength.append(len(i))
print(strlength)