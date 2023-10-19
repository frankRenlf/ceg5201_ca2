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

from matricx_multiply_algorithms.strassen.strassen import execute_strassen
from matricx_multiply_algorithms.strassen.strassen_multiprocessing import execute_strassen_multiprocessing
from default_test import one_pair, one_group, total_groups
from utils.generate_matrics import matrix_pair


def pair_test():
    one_pair(matrix_pair.data[0][0], execute_strassen)
    one_pair(matrix_pair.data[0][0], execute_strassen_multiprocessing)


def group_test():
    one_group(0, matrix_pair.data[0], execute_strassen)
    one_group(0, matrix_pair.data[0], execute_strassen_multiprocessing)


def total_groups_test():
    total_groups(matrix_pair.data, execute_strassen)
    total_groups(matrix_pair.data, execute_strassen_multiprocessing)


if __name__ == "__main__":
    # group_0 = matrix_pair.data[0]
    # results = [strassen(pair[0], pair[1]) for pair in group_0]
    # just for test, so use first for the smallest execution time
    # res = []
    # test1(0, execute_strassen_multiprocessing)
    # group_test()
    pair_test()

