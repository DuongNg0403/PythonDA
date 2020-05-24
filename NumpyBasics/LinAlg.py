import numpy as np 
from numpy.linalg import inv, qr

x = np.array([[1.,2.,3.],[4.,5.,6.]])

y = np.array([[6., 23.], [-1, 7], [8, 9]])

print(x.dot(y))#2x3 dot 3x2 should output 2x2 and equivalent to np.dot(x,y)

print(x@y) #same as 1 line above

"""
    Function    Description
    diag        return the diagonal elements of a square matrix as a 1D array
                Or convert a 1D array into a square matrix with 0's off diagonal

    dot         Matrix multiplication
    trace       sum of the diagonal element
    det         determinant
    eig         return eigenvalues and eigenvectors of a square matrix
    inv         inverse of a square matrix
    pinv        Moore-Penrose pseudo-inverse of a matrix
    qr          QR decomposition
    svd         single value decomposition
    solve       Solve Ax = b for x, where A is a square matrix
    lstsq       Compute least-squares solution to Ax = b
"""
