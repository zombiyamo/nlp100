# -*- coding: utf-8 -*-
from prettyprint import pp
import string

str = "Hi He Lied Because Boron Could Not Oxidize Fluorine. New Nations Might Also Sign Peace Security Clause. Arthur King Can.".translate(None,'.')
strdic = {}
strs = str.split()

for i in range(len(strs)):
	if i in [0, 4, 5, 6, 7, 8, 14, 15, 18]:
		strdic[i+1] = strs[i][0]
	else:
		strdic[i+1] = strs[i][0] + strs[i][1]
print(strdic)