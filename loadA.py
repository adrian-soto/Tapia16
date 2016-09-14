# Adrian Soto
# 2016-09-13
# Institute for Advanced Computational Science
# Stony Brook University
#
import numpy as np


def loadA(Afile, delim=' '):
# Read adjacency matrix from file

    A = np.loadtxt(Afile)
    return A 


# Load all matrices into a numpy.array
A1=loadA('./data/A1.dat')
A2=loadA('./data/A2.dat')
A3=loadA('./data/A3.dat')
A4=loadA('./data/A4.dat')
A5=loadA('./data/A5.dat')


