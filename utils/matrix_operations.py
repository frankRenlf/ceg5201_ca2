# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren, Jiajun.Feng
    @Project : ceg5201_ca2 
    @Product : PyCharm
    @createTime : 2023/10/10 15:48 
    @Email : e1143935@u.nus.edu, e1143293@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : matrix operations, generate and split
"""

import numpy as np


def split_matrix(A):
    row, col = A.shape
    row2, col2 = row // 2, col // 2
    return A[:row2, :col2], A[:row2, col2:], A[row2:, :col2], A[row2:, col2:]


def matrix_multiply(A, B):
    # A 的列数必须等于 B 的行数
    rows_A = len(A)
    cols_A = len(A[0])
    rows_B = len(B)
    cols_B = len(B[0])

    # 初始化结果矩阵 C
    C = [[0 for row in range(cols_B)] for col in range(rows_A)]

    # 只有当 A 的列数等于 B 的行数时，才能进行矩阵乘法
    if cols_A != rows_B:
        return "Cannot multiply the two matrices. Incorrect dimensions."

    # 执行矩阵乘法
    for i in range(rows_A):
        for j in range(cols_B):
            for k in range(cols_A):
                C[i][j] += A[i][k] * B[k][j]
    return C


def split_matrix_4(A):
    row, col = A.shape
    per_row, per_col = row // 4, col // 4
    A11 = A[per_row * 0: per_row * 1, per_col * 0: per_col * 1]
    A12 = A[per_row * 0: per_row * 1, per_col * 1: per_col * 2]
    A13 = A[per_row * 0: per_row * 1, per_col * 2: per_col * 3]
    A14 = A[per_row * 0: per_row * 1, per_col * 3: per_col * 4]

    A21 = A[per_row * 1: per_row * 2, per_col * 0: per_col * 1]
    A22 = A[per_row * 1: per_row * 2, per_col * 1: per_col * 2]
    A23 = A[per_row * 1: per_row * 2, per_col * 2: per_col * 3]
    A24 = A[per_row * 1: per_row * 2, per_col * 3: per_col * 4]

    A31 = A[per_row * 2: per_row * 3, per_col * 0: per_col * 1]
    A32 = A[per_row * 2: per_row * 3, per_col * 1: per_col * 2]
    A33 = A[per_row * 2: per_row * 3, per_col * 2: per_col * 3]
    A34 = A[per_row * 2: per_row * 3, per_col * 3: per_col * 4]

    A41 = A[per_row * 3: per_row * 4, per_col * 0: per_col * 1]
    A42 = A[per_row * 3: per_row * 4, per_col * 1: per_col * 2]
    A43 = A[per_row * 3: per_row * 4, per_col * 2: per_col * 3]
    A44 = A[per_row * 3: per_row * 4, per_col * 3: per_col * 4]
    return A11, A12, A13, A14, A21, A22, A23, A24, A31, A32, A33, A34, A41, A42, A43, A44


class MatrixPair:

    def __init__(self):
        M = [16, 32, 64, 128, 256, 512, 1024, 2048]

        # M = [16, 32, 64, 128]
        NUM_PAIRS = 1
        NUM_GROUPS = 10
        self.data = [self.generate_matrix_pairs(M, NUM_PAIRS) for _ in range(NUM_GROUPS)]

    def generate_matrix_pairs(self, sizes, num_pairs, value_range=(0, 255)):
        matrix_pairs = []
        for size in sizes:
            for _ in range(num_pairs):
                A = np.random.randint(value_range[0], value_range[1] + 1, (size, size))
                B = np.random.randint(value_range[0], value_range[1] + 1, (size, size))
                matrix_pairs.append((A, B))
        return matrix_pairs


# data shape is : NUM_GROUPS*len(M)*2
matrix_pair = MatrixPair()
# print(matrix_pair.data[0][7][1].shape)
