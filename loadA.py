# Adrian Soto
# 2016-09-13
# Institute for Advanced Computational Science
# Stony Brook University
#
import numpy as np


def loadAA(Afile, delim=' '):
# Read adjacency matrix from file

    A = np.loadtxt(Afile)
    return A 


# Load all matrices into a numpy.array
A1=loadA('A1.dat')
A2=loadA('A2.dat')
A3=loadA('A3.dat')
A4=loadA('A4.dat')
A5=loadA('A5.dat')


