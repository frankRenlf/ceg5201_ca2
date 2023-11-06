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
    row_len = len(A)
    column_len = len(B[0])
    cross_len = len(B)
    res_mat = [[0] * column_len] * row_len
    for i in range(row_len):
        for j in range(column_len):
            for k in range(cross_len):
                temp = A[i][k] * B[k][j]
                res_mat[i][j] += temp
    return res_mat


def matrix_multiply_4(A, B):
    C = np.zeros((4, 4))
    C[0][0] = A[0][0] * B[0][0] + A[0][1] * B[1][0] + A[0][2] * B[2][0] + A[0][3] * B[3][0]
    C[0][1] = A[0][0] * B[0][1] + A[0][1] * B[1][1] + A[0][2] * B[2][1] + A[0][3] * B[3][1]
    C[0][2] = A[0][0] * B[0][2] + A[0][1] * B[1][2] + A[0][2] * B[2][2] + A[0][3] * B[3][2]
    C[0][3] = A[0][0] * B[0][3] + A[0][1] * B[1][3] + A[0][2] * B[2][3] + A[0][3] * B[3][3]

    C[1][0] = A[1][0] * B[0][0] + A[1][1] * B[1][0] + A[1][2] * B[2][0] + A[1][3] * B[3][0]
    C[1][1] = A[1][0] * B[0][1] + A[1][1] * B[1][1] + A[1][2] * B[2][1] + A[1][3] * B[3][1]
    C[1][2] = A[1][0] * B[0][2] + A[1][1] * B[1][2] + A[1][2] * B[2][2] + A[1][3] * B[3][2]
    C[1][3] = A[1][0] * B[0][3] + A[1][1] * B[1][3] + A[1][2] * B[2][3] + A[1][3] * B[3][3]

    C[2][0] = A[2][0] * B[0][0] + A[2][1] * B[1][0] + A[2][2] * B[2][0] + A[2][3] * B[3][0]
    C[2][1] = A[2][0] * B[0][1] + A[2][1] * B[1][1] + A[2][2] * B[2][1] + A[2][3] * B[3][1]
    C[2][2] = A[2][0] * B[0][2] + A[2][1] * B[1][2] + A[2][2] * B[2][2] + A[2][3] * B[3][2]
    C[2][3] = A[2][0] * B[0][3] + A[2][1] * B[1][3] + A[2][2] * B[2][3] + A[2][3] * B[3][3]

    C[3][0] = A[3][0] * B[0][0] + A[3][1] * B[1][0] + A[3][2] * B[2][0] + A[3][3] * B[3][0]
    C[3][1] = A[3][0] * B[0][1] + A[3][1] * B[1][1] + A[3][2] * B[2][1] + A[3][3] * B[3][1]
    C[3][2] = A[3][0] * B[0][2] + A[3][1] * B[1][2] + A[3][2] * B[2][2] + A[3][3] * B[3][2]
    C[3][3] = A[3][0] * B[0][3] + A[3][1] * B[1][3] + A[3][2] * B[2][3] + A[3][3] * B[3][3]

    return C


# >>>>>>> 0d0b2eabfbde96c7d1b9d3b419fccc35c3414d32


# # 只有当 A 的列数等于 B 的行数时，才能进行矩阵乘法
# if cols_A != rows_B:
#     return "Cannot multiply the two matrices. Incorrect dimensions."

# # 执行矩阵乘法
# for i in range(rows_A):
#     for j in range(cols_B):
#         for k in range(cols_A):
#             C[i][j] += A[i][k] * B[k][j]
# return C


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
# print(matrix_pair.data[0][0][1].shape)
# if __name__ == "__main__":
#     # code for test
#     c = matrix_pair.data[0][0][0]@matrix_pair.data[0][0][1]
#     c2 = matrix_multiply(matrix_pair.data[0][0][1], matrix_pair.data[0][0][0])
#     print(c[:] == c2[:])
