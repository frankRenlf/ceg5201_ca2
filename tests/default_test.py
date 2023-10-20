# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : ceg5201_ca2 
    @Product : PyCharm
    @createTime : 2023/10/11 09:59 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : default tests: pair, group, groups
"""
import numpy as np

from utils.time_consume import group_timing_decorator, total_timing_decorator


def one_pair(pair, func):
    # test if the algorithm is correct
    tmp = (pair[0], pair[1])
    result = func(*tmp)
    res = np.matmul(pair[0], pair[1])
    print(result[:] == res[:])


@group_timing_decorator
def one_group(group_id, group_, func):
    # test one group, the group_id is the index of the group, and will be shown in the console
    for pair in group_:
        func(pair[0], pair[1])


@total_timing_decorator
def total_groups(data, func):
    # test all groups
    for index, group in enumerate(data):
        one_group(index, group, func)
