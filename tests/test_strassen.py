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
from utils.generate_matrics import matrix_pair
from utils.time_consume import pair_timing_decorator, group_timing_decorator


def one_pair():
    group_0 = matrix_pair.data[0]
    i = 1
    tmp = (group_0[i][0], group_0[i][1])
    result1 = execute_strassen(*tmp)
    result2 = execute_strassen_multiprocessing(*tmp)
    res2 = np.matmul(group_0[i][0], group_0[i][1])
    print(result2[:] == res2[:])

    # print(results[:] == res2[:])


@group_timing_decorator
def one_group(group_id, group_, func):
    res = []
    for pair in group_:
        result1 = func(pair[0], pair[1])
    # res.append(result1)


if __name__ == "__main__":
    # group_0 = matrix_pair.data[0]

    # results = [strassen(pair[0], pair[1]) for pair in group_0]
    # just for test, so use first for the smallest execution time
    # res = []
    # one_pair()
    # one_group(execute_strassen)
    # one_group(execute_strassen_multiprocessing)
    for index, group in enumerate(matrix_pair.data):
        # just test one group
        one_group(index, group, execute_strassen)
        one_group(index, group, execute_strassen_multiprocessing)
        break
    # test1(0, execute_strassen_multiprocessing)
