# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : ceg5201_ca2 
    @Product : PyCharm
    @createTime : 2023/10/10 16:37 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : 
"""

import numpy as np
from multiprocessing import Process, Pipe

from utils.time_consume import timing_decorator


def split_matrix(A):
    row, col = A.shape
    row2, col2 = row // 2, col // 2
    return A[:row2, :col2], A[:row2, col2:], A[row2:, :col2], A[row2:, col2:]


def parallel_strassen(conn, A, B):
    conn.send(strassen(A, B))
    conn.close()


def strassen(A, B):
    if max(A.shape[0], A.shape[1], B.shape[0], B.shape[1]) <= 2:
        return np.dot(A, B)

    A11, A12, A21, A22 = split_matrix(A)
    B11, B12, B21, B22 = split_matrix(B)

    processes = []
    pipes = []

    # 使用multiprocessing进行子矩阵乘法
    for sub_A, sub_B in [(A11 + A22, B11 + B22), (A21 + A22, B11), (A11, B12 - B22),
                         (A22, B21 - B11), (A11 + A12, B22), (A21 - A11, B11 + B12),
                         (A12 - A22, B21 + B22)]:
        parent_conn, child_conn = Pipe()
        pipes.append(parent_conn)
        process = Process(target=parallel_strassen, args=(child_conn, sub_A, sub_B))
        processes.append(process)
        process.start()

    M = [pipe.recv() for pipe in pipes]

    for process in processes:
        process.join()

    C11 = M[0] + M[3] - M[4] + M[6]
    C12 = M[2] + M[4]
    C21 = M[1] + M[3]
    C22 = M[0] - M[1] + M[2] + M[5]

    C = np.vstack((np.hstack((C11, C12)), np.hstack((C21, C22))))
    return C


@timing_decorator
def execute_strassen_multiprocessing(A, B):
    return strassen(A, B)