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
from utils.results_generate import save_to_file


def run_all(data=matrix_pair.data):
    assert data is not None
    # run strassen
    test_strassen.total_groups_test(data)
    # run coppersmith_winograd
    test_coppersmith_winograd.total_groups_test_coppersmith_winograd(data)
    # run others....


def run2terminal():  # print result to terminal
    run_all()


def run2file():  # save result to file
    save_to_file(run_all, "output.txt")


def switch():
    chosen = input("please choose the way to run the test:\n")
    if chosen == '1':
        run2file()
    elif chosen == '2':
        run2terminal()


if __name__ == "__main__":
    switch()
