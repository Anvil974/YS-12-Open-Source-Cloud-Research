#!/usr/bin/python3
#Partially used code from GeeksForGeeks: https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/

import sys

output = {}
for line in sys.stdin:
    line = line.strip()
    word, count = line.split('\t', 1)
    try:
        count = int(count)
    except ValueError:
        continue

    try:
        output[word] = output[word]+count
    except:
        output[word] = count

counter = 0
for k,v in sorted(output.items(), key = lambda kv:(kv[1], kv[0]), reverse=True):
    if(counter==100):
        break
    print("{0}\t{1}".format(k,v))
    counter+=1