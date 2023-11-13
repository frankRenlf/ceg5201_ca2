# -*- coding: UTF-8 -*-
"""
    @Author : Jiajun.FENG
    @Project : ceg5201_ca2 
    @Product : VS Code
    @createTime : 2023/11/05 22:37 
    @Email : e1143293@u.nus.edu
    @github : 
    @Description : test for cannon by using default_test.py
"""

import sys
sys.path.append('/Users/junnnn/Desktop/NUS/Hardware/CA2/ceg5201_ca2')
from tests import default_test

from tests.default_test import one_pair, one_group, total_groups
from matricx_multiply_algorithms.cannon.cannon import execute_cannon
from matricx_multiply_algorithms.cannon.cannon_multiprocessing import execute_parallel_cannon
from utils.matrix_operations import matrix_pair


def pair_test():
    one_pair(matrix_pair.data[0][0], execute_cannon)
    one_pair(matrix_pair.data[0][0], execute_parallel_cannon)


def group_test():
    one_group(0, matrix_pair.data[0], execute_parallel_cannon)
    one_group(0, matrix_pair.data[0], execute_cannon)
    


def total_groups_test(data):
    total_groups(data, execute_cannon)
    total_groups(data, execute_parallel_cannon)

def save_to_file(func, file_name='output.txt'):
    original_stdout = sys.stdout

    with open(file_name, 'a') as f:
        # direct to file
        sys.stdout = f

        # call the function
        func()
        # reset to console
        sys.stdout = original_stdout

if __name__ == "__main__":
    save_to_file(pair_test, "./cannon.txt")



