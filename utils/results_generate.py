# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : ceg5201_ca2 
    @Product : PyCharm
    @createTime : 2023/11/5 19:20 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : 
"""

import sys


def print_to_file(data, file_name='output.txt'):
    original_stdout = sys.stdout

    with open(file_name, 'a') as f:
        # 将标准输出重定向到文件
        sys.stdout = f

        print(data)

        sys.stdout = original_stdout


if __name__ == "__main__":
    print_to_file("hello world")
