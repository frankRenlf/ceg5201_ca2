# -*- coding: UTF-8 -*-
"""
    @Author : Jiajun.FENG
    @Project : ceg5201_ca2 
    @Product : VS Code
    @createTime : 2023/10/30 16:03 
    @Email : e1143293@u.nus.edu
    @github :
    @Description : multiprocessing of cannon algorithm
"""
import multiprocessing
import numpy as np
import sys

sys.path.append('/Users/junnnn/Desktop/NUS/Hardware/CA2/ceg5201_ca2')  # path of the folder
from utils.time_consume import pair_timing_decorator
from utils.matrix_operations import split_matrix_4
from multiprocessing import Pool, cpu_count
import cannon


# combine 16 sub matrices into a large one
def combine_matrix(C11, C12, C13, C14, C21, C22, C23, C24, C31, C32, C33, C34, C41, C42, C43, C44):
    row1 = np.hstack((C11, C12, C13, C14))
    row2 = np.hstack((C21, C22, C23, C24))
    row3 = np.hstack((C31, C32, C33, C34))
    row4 = np.hstack((C41, C42, C43, C44))
    return np.vstack((row1, row2, row3, row4))


def parallel_cannon(A, B):
    return cannon.cannon(A, B)


@pair_timing_decorator
def execute_parallel_cannon(A, B):
    if A.shape[0] < 4 or B.shape[0] < 4:
        return A @ B
    A11, A12, A13, A14, A21, A22, A23, A24, A31, A32, A33, A34, A41, A42, A43, A44 = split_matrix_4(A)
    B11, B12, B13, B14, B21, B22, B23, B24, B31, B32, B33, B34, B41, B42, B43, B44 = split_matrix_4(B)

    # 递归计算16个子矩阵乘法
    C11 = [(A11, B11), (A12, B21), (A13, B31), (A14, B41)]
    C12 = [(A11, B12), (A12, B22), (A13, B32), (A14, B42)]
    C13 = [(A11, B13), (A12, B23), (A13, B33), (A14, B43)]
    C14 = [(A11, B14), (A12, B24), (A13, B34), (A14, B44)]

    C21 = [(A21, B11), (A22, B21), (A23, B31), (A24, B41)]
    C22 = [(A21, B12), (A22, B22), (A23, B32), (A24, B42)]
    C23 = [(A21, B13), (A22, B23), (A23, B33), (A24, B43)]
    C24 = [(A21, B14), (A22, B24), (A23, B34), (A24, B44)]

    C31 = [(A31, B11), (A32, B21), (A33, B31), (A34, B41)]
    C32 = [(A31, B12), (A32, B22), (A33, B32), (A34, B42)]
    C33 = [(A31, B13), (A32, B23), (A33, B33), (A34, B43)]
    C34 = [(A31, B14), (A32, B24), (A33, B34), (A34, B44)]

    C41 = [(A41, B11), (A42, B21), (A43, B31), (A44, B41)]
    C42 = [(A41, B12), (A42, B22), (A43, B32), (A44, B42)]
    C43 = [(A41, B13), (A42, B23), (A43, B33), (A44, B43)]
    C44 = [(A41, B14), (A42, B24), (A43, B34), (A44, B44)]

    tasks = C11 + C12 + C13 + C14 + C21 + C22 + C23 + C24 + C31 + C32 + C33 + C34 + C41 + C42 + C43 + C44

    with Pool(processes=cpu_count()) as pool:
        results = pool.starmap(parallel_cannon, tasks)

    # Combine to form the sub-matrices of C
    C_sub = []
    for i in range(0, len(results), 4):
        sum_matrix = results[i]

        for matrix in results[i + 1:i + 4]:
            sum_matrix += matrix

        C_sub.append(sum_matrix)
    C = combine_matrix(*C_sub)
    return C

# codes for test
# A = np.random.rand(1024, 1024)
# B = np.random.rand(1024, 1024)

# C_parallel = execute_parallel_cannon(A, B)

# assert np.allclose(C_parallel, A @ B, atol=1e-6)
# print("Parallel Cannon: correct!")
