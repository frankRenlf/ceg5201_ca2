# -*- coding: UTF-8 -*-
"""
    @Author : Jiajun.FENG
    @Project : ceg5201_ca2 
    @Product : VS Code
    @createTime : 2023/10/30 16:03 
    @Email : e1143293@u.nus.edu
    @github :
    @Description : sequential cannon algorithm
"""

import numpy as np
import sys
sys.path.append('/Users/junnnn/Desktop/NUS/Hardware/CA2/ceg5201_ca2')  # path of the folder
from utils.time_consume import pair_timing_decorator
from utils.matrix_operations import split_matrix_4

# combine 16 sub matrices into a large one
def combine_matrix(C11, C12, C13, C14, C21, C22, C23, C24, C31, C32, C33, C34, C41, C42, C43, C44):
    row1 = np.hstack((C11, C12, C13, C14))
    row2 = np.hstack((C21, C22, C23, C24))
    row3 = np.hstack((C31, C32, C33, C34))
    row4 = np.hstack((C41, C42, C43, C44))
    return np.vstack((row1, row2, row3, row4))
def cannon(A, B):
    if A.shape[0] <= 4 or B.shape[0] <= 4:
        return A @ B
    A11, A12, A13, A14, A21, A22, A23, A24, A31, A32, A33, A34, A41, A42, A43, A44 = split_matrix_4(A)
    B11, B12, B13, B14, B21, B22, B23, B24, B31, B32, B33, B34, B41, B42, B43, B44 = split_matrix_4(B)

    # 
    C11 = cannon(A11, B11) + cannon(A12, B21) + cannon(A13, B31) + cannon(A14, B41)
    C12 = cannon(A11, B12) + cannon(A12, B22) + cannon(A13, B32) + cannon(A14, B42)
    C13 = cannon(A11, B13) + cannon(A12, B23) + cannon(A13, B33) + cannon(A14, B43)
    C14 = cannon(A11, B14) + cannon(A12, B24) + cannon(A13, B34) + cannon(A14, B44)
    
    C21 = cannon(A21, B11) + cannon(A22, B21) + cannon(A23, B31) + cannon(A24, B41)
    C22 = cannon(A21, B12) + cannon(A22, B22) + cannon(A23, B32) + cannon(A24, B42)
    C23 = cannon(A21, B13) + cannon(A22, B23) + cannon(A23, B33) + cannon(A24, B43)
    C24 = cannon(A21, B14) + cannon(A22, B24) + cannon(A23, B34) + cannon(A24, B44)
    
    C31 = cannon(A31, B11) + cannon(A32, B21) + cannon(A33, B31) + cannon(A34, B41)
    C32 = cannon(A31, B12) + cannon(A32, B22) + cannon(A33, B32) + cannon(A34, B42)
    C33 = cannon(A31, B13) + cannon(A32, B23) + cannon(A33, B33) + cannon(A34, B43)
    C34 = cannon(A31, B14) + cannon(A32, B24) + cannon(A33, B34) + cannon(A34, B44)
    
    C41 = cannon(A41, B11) + cannon(A42, B21) + cannon(A43, B31) + cannon(A44, B41)
    C42 = cannon(A41, B12) + cannon(A42, B22) + cannon(A43, B32) + cannon(A44, B42)
    C43 = cannon(A41, B13) + cannon(A42, B23) + cannon(A43, B33) + cannon(A44, B43)
    C44 = cannon(A41, B14) + cannon(A42, B24) + cannon(A43, B34) + cannon(A44, B44)

    return combine_matrix(C11, C12, C13, C14, C21, C22, C23, C24, C31, C32, C33, C34, C41, C42, C43, C44)


@pair_timing_decorator
def execute_cannon(A, B):
    return cannon(A, B)

if __name__ == "__main__":
    # code for test
    A = np.random.rand(1024, 1024)
    B = np.random.rand(1024, 1024)
    C = execute_cannon(A, B)

    assert np.allclose(C, A @ B)
    print("Cannon Output: Corret")