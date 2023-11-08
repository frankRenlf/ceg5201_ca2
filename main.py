# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : ceg5201_ca2 
    @Product : PyCharm
    @createTime : 2023/10/20 09:49 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : if you want to run all tests, just run this file
"""
from utils.matrix_operations import matrix_pair
from tests import test_strassen
from tests import test_coppersmith_winograd


def run_all(data=matrix_pair.data):
    assert data is not None
    # run strassen
    test_strassen.total_groups_test(data)
    # run coppersmith_winograd
    test_coppersmith_winograd.total_groups_test_coppersmith_winograd(data)
    # run others....


if __name__ == "__main__":
    run_all()
