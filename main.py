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


def run_all():
    # run strassen
    test_strassen.total_groups_test(matrix_pair.data)
    # run others....


if __name__ == "__main__":
    run_all()