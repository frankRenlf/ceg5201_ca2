# -*- coding: UTF-8 -*-
"""

"""


from matricx_multiply_algorithms.coppersmith_winograd.coppersmith_winograd import execute_coppersmith_winograd, \
    coppersmith_winograd
from matricx_multiply_algorithms.coppersmith_winograd.coppersmith_winograd_multiprocessing import \
    execute_coppersmith_winograd_multiprocessing
from tests.default_test import one_pair, one_group, total_groups
from utils.matrix_operations import matrix_pair


def pair_test_coppersmith_winograd():
    one_pair(matrix_pair.data[0][0], execute_coppersmith_winograd)
    one_pair(matrix_pair.data[0][0], execute_coppersmith_winograd_multiprocessing)


def group_test_coppersmith_winograd():
    one_group(0, matrix_pair.data[0], execute_coppersmith_winograd)
    one_group(0, matrix_pair.data[0], execute_coppersmith_winograd_multiprocessing)


def total_groups_test_coppersmith_winograd(data):
    total_groups(data, execute_coppersmith_winograd)
    total_groups(data, execute_coppersmith_winograd_multiprocessing)


if __name__ == "__main__":
    group_0 = matrix_pair.data[0]
    # results = [coppersmith_winograd(pair[0], pair[1]) for pair in group_0]
    # just for test, so use first for the smallest execution time
    # res = []
    # test1(0, execute_coppersmith_winograd_multiprocessing)
    # group_test_coppersmith_winograd()
    # print('++++++++++++++++++++++++++++++++')
    # pair_test_coppersmith_winograd()
    # results = [coppersmith_winograd(pair[0], pair[1]) for pair in matrix_pair.data]
    total_groups_test_coppersmith_winograd(matrix_pair.data)
    print('finish')
