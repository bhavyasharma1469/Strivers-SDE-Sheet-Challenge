from math import *
from collections import *
from sys import *
from os import *

from typing import List

def setZeros(m: List[List[int]]) -> None:
	# Write your code here.
    r = set()
    c = set()
    for i in range(len(m)):
        for j in range(len(m[0])):
            if m[i][j] == 0:
                r.add(i)
                c.add(j)
    for i in r:
        for j in range(len(m[0])):
            m[i][j] = 0

    for j in c:
        for i in range(len(m)):
            m[i][j] = 0        
                       

    pass
