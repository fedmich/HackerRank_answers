#!/bin/python

import sys

n = int(raw_input().strip())

# Test cases
# n = 6

for i in range( 1, n +1):
	print ' ' * (n-i) + '#' * i  