# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : ceg5201_ca2 
    @Product : PyCharm
    @createTime : 2023/10/10 16:37 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : multiprocessing version of strassen
"""

import numpy as np
from utils.time_consume import pair_timing_decorator
from multiprocessing import Pool, cpu_count
from utils.matrix_operations import split_matrix


def parallel_strassen(args):
    return strassen_multiprocessing(args[0], args[1], args[2])


def strassen_multiprocessing(A, B, depth=0, max_depth=1):
    if A.shape[0] < 2 or B.shape[0] < 2:
        return A * B
    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    args = [[A11 + A21, B11 + B12], [A12 + A22, B21 + B22], [A11 - A22, B11 + B22],
            [A11, B12 - B22], [A21 + A22, B11], [A11 + A12, B22],
            [A22, B21 - B11]]
    if depth < max_depth:
        # cpu_count() will return 12 in my computer, but subtasks will be 7, so it only open 7 processes
        with Pool(processes=7) as pool:
            args_a = [el + [depth + 1] for el in args]
            M = pool.map(parallel_strassen, args_a)
    else:
        M = [strassen_multiprocessing(a[0], a[1], depth + 1, max_depth) for a in args]

    C11 = M[1] + M[2] - M[5] - M[6]
    C12 = M[3] + M[5]
    C21 = M[4] + M[6]
    C22 = M[0] - M[2] - M[3] - M[4]

    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C


@pair_timing_decorator
def execute_strassen_multiprocessing(A, B):
    return strassen_multiprocessing(A, B)
