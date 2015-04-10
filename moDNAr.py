#!/usr/bin/env python

import sys, random

# Prompt for sequence length 
print "How many bases?"
n = input()

# Markov probability chain matrix for each base
# Data obtained from janey.yu@cs.helsinki.f
pm = {'a' : {'a' : 0.359, 'c' : 0.143, 'g' : 0.167, 't' : 0.331},
'c' : {'a' : 0.384, 'c' : 0.156, 'g' : 0.023, 't' : 0.437},
'g' : {'a' : 0.305, 'c' : 0.199, 'g' : 0.150, 't' : 0.345},
't' : {'a' : 0.284, 'c' : 0.182, 'g' : 0.177, 't' : 0.357}}

# Overall frequencies 
pi = {'a' : 0.328, 'c' : 0.167, 'g' : 0.144, 't' : 0.360}

# Function to pick key based on probability matrix
def choose(dist):
    r = random.random()
    sum = 0.0
    keys = dist.keys()
    for k in keys:
        sum = sum + dist[k]
        if sum > r:
                return k
    return keys[-1]

# Determines first base, then subsequent bases
c = choose(pi)
for i in range(n - 1):
    sys.stdout.write(c)
    c = choose(tm[c])
sys.stdout.write(c)
sys.stdout.write("\n")
