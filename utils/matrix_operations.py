# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : ceg5201_ca2 
    @Product : PyCharm
    @createTime : 2023/10/10 15:48 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : matrix operations, generate and split
"""

import numpy as np


def split_matrix(A):
    row, col = A.shape
    row2, col2 = row // 2, col // 2
    return A[:row2, :col2], A[:row2, col2:], A[row2:, :col2], A[row2:, col2:]


class MatrixPair:

    def __init__(self):
        M = [16, 32, 64, 128, 256, 512, 1024, 2048]
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
