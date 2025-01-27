#!/usr/bin/env python
# Samuel Shepard - doSVM - 9.2011
# Tests unknown sequences for the genotyping system.
# The load_matrix function is given below and taken
# from the SHOGUN toolkit help files.
from numpy import double, fromfile
from sg import sg
import sys

# Courtesy the Shogun Toolkit 1.0.0
# Soeren Sonnenburg et al. 2010
# http://www.shogun-toolbox.org/
# load.py in examples/undocumented/python_static/tools
# modified for arbritrary lines in the file
def load_numbers(filename):
	matrix=fromfile(filename, sep=' ')
	# whole matrix is 1-dim now, so reshape
	L=len(open(filename).readlines())
	matrix=matrix.reshape(L, len(matrix)/L)
	return matrix

def load_labels(filename):
	return fromfile(filename, dtype=double, sep=' ')

# ARG LIST:
# doSVM.py GROUP TRAIN LABEL TEST RESULT


# Instantiate variables.
size_cache=20
degree=20
inhomogene=True
use_normalization=True

# Load data.
alist=sys.argv
traindata=load_numbers( alist[2] )
labels=load_labels( alist[3] )
testdata=load_numbers( alist[4] )

# Perform classification
sg('new_classifier', 'GMNPSVM')
sg('set_kernel', 'POLY', 'REAL', size_cache, degree, inhomogene, use_normalization)
sg('set_features', 'TRAIN', traindata)
sg('set_labels', 'TRAIN', labels)
sg('train_classifier')
sg('save_classifier', './myClassifier.txt')
sg('set_features', 'TEST', testdata)
R=sg('classify')
kernel_matrix = sg('get_kernel_matrix', 'TEST')


# Output results.
fp=open( alist[5], "a")
for i in range(len(R)):
	fp.write("%d\t%d\t%s\n" % ((i+1), R[i], alist[1]) )
fp.close()
