# -*- coding: utf-8 -*-
# ngramとは...文章などで隣り合うn個の事
# 単語ngramならngram関数に単語のリスト,文字ngramなら文字のリストを渡せばよい
# hoge

def ngram(list,n):
	results = []
	if len(list) >= n:
		for i in xrange(len(list)-n+1):
			results.append(list[i:i+n])
	return results


text = 'I am an NLPer'
wordList = text.split()
charList = text.replace(' ','')
print ngram(wordList, 2)
print ngram(charList, 2)