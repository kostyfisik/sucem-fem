# Authors:
# Evan Lezar <mail@evanlezar.com>

"""This file contains a number of converters, including for DOLFIN matrices to scipy sparse matrices"""

import numpy as np
import dolfin

def dolfin_ublassparse_to_scipy_csr ( A, dtype=None, imagify=False ):
    """
    convert a DOLFIN uBLASSparseMatrix to a scipy.sparse.csr_matrix()
    
    @param A: a DOLFIN uBLASSparseMatrix
    @param dtype: the numpy data type to use to store the matrix
    @param imagify: multiply the original matrix data by 1j
    """
    import scipy.sparse
    # get the sparse data from the input matrix
    (row,col,data) = A.data()   # get sparse data
    col = np.intc(col)
    row = np.intc(row)
    n = A.size(0)
    if imagify: data = data*1j
    A_sp = scipy.sparse.csr_matrix( (data,col,row), shape=(n,n), dtype=dtype)
    
    return A_sp

def as_dolfin_vector(a):
    """Convert array to a dolfin Vector() instance"""
    assert len(a.shape) == 1            # 1D vectors please
    v = dolfin.Vector(len(a))
    v.set_local(np.require(a, requirements=['C',]))
    return v

