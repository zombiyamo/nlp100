# -*- coding: utf-8 -*-
import sys

args = sys.argv

if len(args) == 3:
    list = []
    index = 0
    # 分割する行数
    divNum = int(sum(1 for i in open(args[1])) / int(args[2]))
    # 1行ずつリストに格納
    for line in open(args[1]):
        list.append(line)

    # divNum * index+1までの行をファイルに追記
    # 書き込みでできたほうが良い気がする
    for i, x in enumerate(list):
        if i < divNum * (index+1):
            with open(args[1].replace('.txt', str(index) + '.txt'), 'a') as f:
                f.write(x)
        else:
            index += 1
