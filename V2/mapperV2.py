#!/usr/bin/python3
#Coden taken from GeeksForGeeks: https://www.geeksforgeeks.org/hadoop-streaming-using-python-word-count-problem/

import sys

for line in sys.stdin:
    
    line = line.strip()
    words = line.split()
    
    for word in words:
        print('%s\t%s' % (word, 1))
