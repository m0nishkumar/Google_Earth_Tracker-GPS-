#!/usr/bin/env python
import sys
x=sys.argv[1]
for i in range(1,len(x)+1):
    for j in range(0,i): 
        print(x[j])
    print("/n")

