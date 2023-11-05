# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : ceg5201_ca2 
    @Product : PyCharm
    @createTime : 2023/10/10 16:37 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : test for strassen by using default_test.py
"""
from matricx_multiply_algorithms.strassen.strassen import execute_strassen
from matricx_multiply_algorithms.strassen.strassen_multiprocessing import execute_strassen_multiprocessing
from default_test import one_pair, one_group, total_groups
from utils.matrix_operations import matrix_pair
from utils.results_generate import print_to_file


def pair_test():
    one_pair(matrix_pair.data[0][2], execute_strassen)
    one_pair(matrix_pair.data[0][2], execute_strassen_multiprocessing)


def group_test():
    one_group(0, matrix_pair.data[0], execute_strassen)
    one_group(0, matrix_pair.data[0], execute_strassen_multiprocessing)


def total_groups_test(data):
    total_groups(data, execute_strassen)
    total_groups(data, execute_strassen_multiprocessing)


if __name__ == "__main__":
    # group_0 = matrix_pair.data[0]
    # results = [strassen(pair[0], pair[1]) for pair in group_0]
    # just for test, so use first for the smallest execution time
    # res = []
    # test1(0, execute_strassen_multiprocessing)
    print_to_file(pair_test, "./strassen.txt")

    # pair_test()
