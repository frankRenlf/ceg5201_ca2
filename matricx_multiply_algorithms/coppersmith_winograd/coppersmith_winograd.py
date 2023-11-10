# -*- coding: UTF-8 -*-
"""
    @Author : YICHENG LUO
    @Project : ceg5201_ca2
    @Product : PyCharm
    @createTime : 2023/10/20 09:49
    @Email : e1143579@u.nus.edu
    @github : https://github.com/GH-YC-L
    @Description :
"""

import numpy as np

from utils.time_consume import pair_timing_decorator
from utils.matrix_operations import split_matrix

def coppersmith_winograd(X, Y):
    if X.shape[0] < 2 or Y.shape[0] < 2:
        return X * Y
    X11, X12, X21, X22 = split_matrix(X)
    Y11, Y12, Y21, Y22 = split_matrix(Y)

    S1 = X21 + X22
    S2 = S1 - X11
    S3 = X11 - X21
    S4 = X12 + S2

    T1 = Y12 - Y11
    T2 = Y22 - T1
    T3 = Y22 - Y12
    T4 = T2 - Y21

    args = [[X11, Y11], [X12, Y21], [S4, Y22], [X22, T4], [S1, T1], [S2, T2], [S3, T3]]
    #           M1           M2        M3          M4        M5        M6        M7
    M = [coppersmith_winograd(a[0], a[1]) for a in args]

    Z11 = M[0] + M[1]
    Z12 = M[0] + M[1] + M[4] + M[5]
    Z21 = M[6] - M[4]
    Z22 = M[0] + M[3] + M[4] + M[6]

    Z = np.vstack((np.hstack((Z11, Z12)), np.hstack((Z21, Z22))))
    return Z

@pair_timing_decorator
def execute_coppersmith_winograd(A, B):
    return coppersmith_winograd(A, B)