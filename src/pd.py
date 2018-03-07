####################
# Support functions to deal with product distributions
# March 2018
####################

import numpy as np


## Pre:
#	k:	number of normalized rows
## Post:
#	k*1 array with normalized rows of random values
def normalizedVector(k):
	res = np.ndarray(shape=(k), dtype='float')
	for i in range(k):
		tmp = np.random.randint(1,50) # can be used to control error
		res[i] = tmp
	normalizer = res.sum(axis=0)
	return res/normalizer

## Pre:
# 	n:	lenght of the product distributions [n > 0]
#	b:	number of discrete values that the
#		product distribution can get [b > 1]
#	k:	number of product distributions [k > 1]
## Post:
#	tuple with
#	1. 	k*n*b array with k n-sized product distributions
# 		over b discrete values
#	2. 	k*1 array with mixture rates
## Format:
#	acces column j of distribution i -> dist[i,j,:]
#	access mixing i mixing rates -> rates[i]
def prodDistGen(k,n,b):
	dist = np.ndarray(shape=(k,n,b), dtype='float')
	for i in range(k):
		for j in range(n):
			dist[i,j,:] = normalizedVector(b)
	rates = normalizedVector(k)
	return dist, rates

## Pre:
#	dist:	array of product distribution means of size n
#	rates:	mixing rates of product distributions
#	m:		number of samples required
## Post:
#	m*n	matrix with rows contaning samples from the given product distribution
## Format:
#	access samples i -> samples[i,:]
def prodDistSample(dist,rates,m):
	n = dist.shape[1]
	b = dist.shape[2]
	k = rates.shape[0]
	samples = np.ndarray(shape=(m,n), dtype='int')
	for i in range(m):
		for j in range(n):
			r = np.random.choice(k,p=rates)
			samples[i,j] = np.random.choice(b,p=dist[r,j,:])
	return samples
