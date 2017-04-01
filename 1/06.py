# -*- coding: utf-8 -*-


def ngram(text, n):
    results = []
    if len(text) >= n:
        for i in xrange(len(text)-n+1):
            results.append(text[i:i+n])
    return results


X = ngram("paraparaparadise", 2)
Y = ngram("paragraph", 2)

union = X + Y
print union


diff = list(set(X).difference(set(Y)))
print diff


product = list(set(X).intersection(set(Y)))
print product

# リスト連結
# X.extend(Y)
# print "union:",X

# NG extendはリスト自身を拡張するメソッドなのでextendの返り値はNone
# print X.extend -> None
