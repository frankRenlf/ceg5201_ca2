# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : ceg5201_ca2 
    @Product : PyCharm
    @createTime : 2023/10/10 16:03 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : sequential strassen algorithm
"""

import numpy as np

from utils.time_consume import pair_timing_decorator
from utils.matrix_operations import split_matrix


def strassen(A, B):
    if A.shape[0] < 2 or B.shape[0] < 2:
        return A * B
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    args = [[A11 + A21, B11 + B12], [A12 + A22, B21 + B22], [A11 - A22, B11 + B22],
            [A11, B12 - B22], [A21 + A22, B11], [A11 + A12, B22],
            [A22, B21 - B11]]

    M = [strassen(a[0], a[1]) for a in args]

    C11 = M[1] + M[2] - M[5] - M[6]
    C12 = M[3] + M[5]
    C21 = M[4] + M[6]
    C22 = M[0] - M[2] - M[3] - M[4]

    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C


@pair_timing_decorator
def execute_strassen(A, B):
    return strassen(A, B)
