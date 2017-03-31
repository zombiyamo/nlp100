# -*- coding: utf-8 -*-
from prettyprint import pp

str = []
for i in zip(u"パトカー", u"タクシー"):
	for j in i:
		str.append("".join(j))
print("".join(str))
