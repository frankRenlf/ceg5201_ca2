# -*- coding: UTF-8 -*-
import numpy as np
import sys
sys.path.append(r"C:/Users/Harrison/Desktop/Sg2023/Semaster 1/CEG 5201 hardware/CA announce/ceg5201_ca2")
from matricx_multiply_algorithms.fox.fox import execute_fox
from matricx_multiply_algorithms.fox.fox_multiprocessing import execute_fox_multiprocessing
from default_test import one_pair, one_group, total_groups
from utils.matrix_operations import matrix_pair
from utils.results_generate import save_to_file


def pair_test():
    one_pair(matrix_pair.data[0][0], execute_fox)
    one_pair(matrix_pair.data[0][0], execute_fox_multiprocessing)


def group_test(num):
    # one_group(0, matrix_pair.data[0], execute_fox)
    one_group(0, matrix_pair.data[0], execute_fox_multiprocessing, num)


def total_groups_test(data):
    total_groups(data, execute_fox)
    total_groups(data, execute_fox_multiprocessing)


if __name__ == "__main__":
    group_0 = matrix_pair.data[0]
    # results = [strassen(pair[0], pair[1]) for pair in group_0]
    # just for test, so use first for the smallest execution time
    # res = []
    # test1(0, execute_strassen_multiprocessing)
    # for i in range(6):
    #     print(7-i)
    #     group_test(7-i)
    group_test(1)
    # pair_test(
    # save_to_file(to-tal_groups_test(matrix_pair.data), "./matricx_multiply_algorithms/fox/total.txt")
    # total_groups_test(matrix_pair.data)
    print('finish')