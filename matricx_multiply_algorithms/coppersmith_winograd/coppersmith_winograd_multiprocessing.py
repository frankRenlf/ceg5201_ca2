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
from multiprocessing import Pool, cpu_count
from utils.matrix_operations import split_matrix


def parallel_coppersmith_winograd(args):
    return coppersmith_coppersmith_winograd_multiprocessing(args[0], args[1], args[2])


def coppersmith_coppersmith_winograd_multiprocessing(X, Y, depth=0, max_depth=1):
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
    #           W1           W2        W3          W4        W5        W6        W7
    if depth < max_depth:
        with Pool(processes=cpu_count()) as pool:
        # with Pool(processes=3) as pool:
            args_a = [el + [depth + 1] for el in args]
            M = pool.map(parallel_coppersmith_winograd, args_a)
    else:
        M = [coppersmith_coppersmith_winograd_multiprocessing(a[0], a[1], depth + 1, max_depth) for a in args]

    Z11 = M[0] + M[1]
    Z12 = M[0] + M[1] + M[4] + M[5]
    Z21 = M[6] - M[4]
    Z22 = M[0] + M[3] + M[4] + M[6]

    Z = np.vstack((np.hstack((Z11, Z12)), np.hstack((Z21, Z22))))
    return Z

@pair_timing_decorator
def execute_coppersmith_winograd_multiprocessing(A, B):
    return coppersmith_coppersmith_winograd_multiprocessing(A, B)