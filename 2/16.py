# -*- coding: utf-8 -*-
import sys

args = sys.argv

if len(args) == 3:
    list = []
    N = args[2]
    # 分割する行数
    divNum = int(sum(1 for i in open(args[1])) / int(N))
    # 1行ずつリストに格納
    for line in open(args[1]):
        list.append(line)

    for i in xrange(0, int(N)):
        with open(args[1].replace('.txt', str(i) + '.txt'), 'w') as f:
            for j in xrange(divNum * i, divNum * (i+1)):
                f.write(list[j])
