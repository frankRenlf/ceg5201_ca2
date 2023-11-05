# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : ceg5201_ca2 
    @Product : PyCharm
    @createTime : 2023/11/5 19:20 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : write the results to file
"""

import sys


def print_to_file(func, file_name='output.txt'):
    original_stdout = sys.stdout

    with open(file_name, 'a') as f:
        # direct to file
        sys.stdout = f
        # call the function
        func()
        # reset to console
        sys.stdout = original_stdout


if __name__ == "__main__":
    print_to_file("hello world")
