#!/usr/bin/env python

import sys
if __name__=="__main__":
    dict_unique = {}   
    while True :
        line=sys.stdin.readline()
        if len(line)<=0:
            break
        item = line.strip()
        if dict_unique.has_key(item):
            continue
        dict_unique[item] = 1
        print "%s"%(item)
