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
from multiprocessing import cpu_count

import numpy as np

from strassen.strassen import execute_strassen
from strassen.strassen_multiprocessing import execute_strassen_multiprocessing
from utils.generate_matrics import matrix_pair


def one_pair():
    i = 5
    tmp = (group_0[i][0], group_0[i][1])
    result1 = execute_strassen(*tmp)
    result2 = execute_strassen_multiprocessing(*tmp)
    res2 = np.matmul(group_0[0][0], group_0[0][1])

    # print(result2[:] == res2[:])

    # print(results[:] == res2[:])


if __name__ == "__main__":
    group_0 = matrix_pair.data[0]

    # results = [strassen(pair[0], pair[1]) for pair in group_0]
    # just for test, so use first for the smallest execution time
    # res = []
    # for pair in group_0:
    #     result1 = execute_strassen(pair[0], pair[1])
    #     res.append(result1)
    one_pair()
