# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : ceg5201_ca2 
    @Product : PyCharm
    @createTime : 2023/10/10 16:03 
    @Email : sc19lr@leeds.ac.uk
    @github : https://github.com/frankRenlf
    @Description : 
"""

from generate_matrics import matrix_pair

import numpy as np


def split_matrix(A):
    row, col = A.shape
    row2, col2 = row // 2, col // 2
    return A[:row2, :col2], A[:row2, col2:], A[row2:, :col2], A[row2:, col2:]


def strassen(A, B):
    if A.shape[0] <= 2 or B.shape[0] <= 2:
        return np.matmul(A, B)

    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    M1 = strassen(A11 + A22, B11 + B22)
    M2 = strassen(A21 + A22, B11)
    M3 = strassen(A11, B12 - B22)
    M4 = strassen(A22, B21 - B11)
    M5 = strassen(A11 + A12, B22)
    M6 = strassen(A21 - A11, B11 + B12)
    M7 = strassen(A12 - A22, B21 + B22)

    C11 = M1 + M4 - M5 + M7
    C12 = M3 + M5
    C21 = M2 + M4
    C22 = M1 - M2 + M3 + M6

    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))

    return C


if __name__ == "__main__":
    group_0 = matrix_pair.data[0]

    # results = [strassen(pair[0], pair[1]) for pair in group_0]
    # just for test, so use first for the smallest execution time
    results = strassen(group_0[0][0], group_0[0][1])
    res2 = np.matmul(group_0[0][0], group_0[0][1])
    print(results[:] == res2[:])
