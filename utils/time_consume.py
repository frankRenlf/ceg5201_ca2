# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : ceg5201_ca2 
    @Product : PyCharm
    @createTime : 2023/10/10 16:34 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : 
"""
import time


def timing_decorator(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"{func.__name__}, matricx shape {args[0].shape}, took {elapsed_time:.5f} seconds to execute.")
        return result

    return wrapper
