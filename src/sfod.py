####################
# Implementation of the algorithm presented on
# 'Learning mixtures of product distributions over discrete domains'
# by Serveido Feldman and O'Donnell
#	https://doi.org/10.1137/060670705
# March 2018
####################

import numpy as np
import itertools as it

## Pre:
#	epsilon:	error bound
#	delta:		probability of failure
#	samples:	m*n matrix with m samples from the original mixture
#	b:			number of values that the product distributions can take
#	k:			number of product distributions mixed
## Post:
#	adist:	array of the approximatated means of the product distributions
#	arates:	approximate mixing rates of product distributions
## Assumtions:
#	the original prodict distributions on the mixtures has a non-negligible
#	distance between them
def ServeidoFeldmanODonnell(epsilon,delta,samples,b,k):
	n = samples.shape[1]
	m = samples.shape[0]

	# define parameters
	epsilon_wts = epsilon**3
	tau = epsilon**2/n**2
	epsilon_mat = tau**(k+1)

	# grid over mixing weights
	for rates in it.product(np.arange(epsilon_wts,1,epsilon_wts),repeat=k):
		# eliminate too small thresholds
		rates = np.array(rates)
		rates = rates[rates < epsilon-epsilon_wts]
		if rates.shape[0] < k: continue

		# obtain the empirical correlation of data
		B = np.zeros([m,m])
		for i in range(m):
			for j in range(i+1,m):
				B[i][j] = np.dot(samples[i,:],samples[j,:])
				B[j][i] = np.dot(samples[i,:],samples[j,:])

		# create matrices of unknowns looping for all possible ranks of M
		for r in range(1,k+1):
			if r != k: continue # only full rank considered TODO

			# try all possible vectors of M (in order to bump into othogonal)
			for idx in it.combinations(range(n), r):
				# take the selected columns from the empirical covariance
				Bk = B[np.array(idx)]

				# grid over all possible vectors in Mj
				for Mj in it.product(it.product(np.arange(-1,1,0.5),repeat=k),repeat=k):
					Mj = np.array(Mj)

					# expand M to have full ranks TODO, B has 0 in the k-r entries

					# if singular matrix skip
					if np.linalg.matrix_rank(Mj) < k: continue
					# solve Mi = B*Mj'
					Mi = np.linalg.solve(Mj,Bk)

					# adapt Mi to be the estimate for the product distribution
					#Mi = Mi.transpose()/np.sqrt(rates)
					print(Mi)
					print(Mj)
					print(B)
					exit(0)
