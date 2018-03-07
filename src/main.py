#!/bin/python3

from fm import FreundMansour
from sfod import ServeidoFeldmanODonnell
from pd import prodDistGen, prodDistSample

# genrate product distribution
k = 3   # number of product distributions
n = 2   # lenght of product distributions
b = 2   # values prod dist can take
dist, rates = prodDistGen(k,n,b)
print('distribution:',dist,'\n')
print('mixing rates:',rates,'\n')

# sample from product distribution
m = 20  # number of samples
samples = prodDistSample(dist,rates,m)
print('samples:',samples,'\n')

# FreundMansour()

# ServeidoFeldmanODonnell()
