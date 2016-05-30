#!/bin/python

import sys


n = int(raw_input().strip())
a = []
for a_i in xrange(n):
    a_temp = map(int,raw_input().strip().split(' '))
    a.append(a_temp)

#print a[2][2]

sum1 = 0
for i in xrange( n  ):
    sum1 += a[i][i]

sum2 = 0
for j in xrange( n -1 , -1 , -1  ):
    #print a[  n - j - 1  ][j]
    sum2 += a[  n - j - 1  ][j]

#print sum1
#print sum2
print abs( sum1 - sum2 )


    