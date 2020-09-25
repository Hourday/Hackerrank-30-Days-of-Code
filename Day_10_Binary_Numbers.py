#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input())
    n=bin(n)[2:]
    l=list(n)
    #print(n)
    s=0
    temp=[]
    for x in l:
        if x=="1":
            s+=1
            temp.append(s)
        elif x=="0":
            s=0
    print(max(temp))
