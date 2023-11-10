# -*- coding: UTF-8 -*-
"""
Wang Hengxu
A0279774E
"""
import numpy as np
import sys
sys.path.append(r"C:/Users/Harrison/Desktop/Sg2023/Semaster 1/CEG 5201 hardware/CA announce/ceg5201_ca2")
from utils.time_consume import pair_timing_decorator
from utils.matrix_operations import split_matrix_4, matrix_multiply


def combine_matrix(C11, C12, C13, C14, C21, C22, C23, C24, C31, C32, C33, C34, C41, C42, C43, C44):
    top_half = np.hstack((np.vstack((C11, C21)), np.vstack((C12, C22)), np.vstack((C13, C23)), np.vstack((C14, C24))))
    bottom_half = np.hstack((np.vstack((C31, C41)), np.vstack((C32, C42)), np.vstack((C33, C43)), np.vstack((C34, C44))))
    return np.vstack((top_half, bottom_half))

def fox(A, B):
    if A.shape[0] <= 4 or B.shape[0] <= 4:
        return matrix_multiply(A, B)
    A11, A12, A13, A14, A21, A22, A23, A24, A31, A32, A33, A34, A41, A42, A43, A44 = split_matrix_4(A)
    B11, B12, B13, B14, B21, B22, B23, B24, B31, B32, B33, B34, B41, B42, B43, B44 = split_matrix_4(B)

    C11 = fox(A11, B11) + fox(A12, B21) + fox(A13, B31) + fox(A14, B41)
    C12 = fox(A12, B22) + fox(A13, B32) + fox(A14, B42) + fox(A11, B12)
    C13 = fox(A13, B33) + fox(A14, B43) + fox(A11, B13) + fox(A12, B23)
    C14 = fox(A14, B44) + fox(A11, B14) + fox(A12, B24) + fox(A13, B34)
    
    C21 = fox(A21, B11) + fox(A22, B21) + fox(A23, B31) + fox(A24, B41)
    C22 = fox(A22, B22) + fox(A23, B32) + fox(A24, B42) + fox(A21, B12)
    C23 = fox(A23, B33) + fox(A24, B43) + fox(A21, B13) + fox(A22, B23)
    C24 = fox(A24, B44) + fox(A21, B14) + fox(A22, B24) + fox(A23, B34)
    
    C31 = fox(A31, B11) + fox(A32, B21) + fox(A33, B31) + fox(A34, B41)
    C32 = fox(A32, B22) + fox(A33, B32) + fox(A34, B42) + fox(A31, B12)
    C33 = fox(A33, B33) + fox(A34, B43) + fox(A31, B13) + fox(A32, B23)
    C34 = fox(A34, B44) + fox(A31, B14) + fox(A32, B24) + fox(A33, B34)
    
    C41 = fox(A41, B11) + fox(A42, B21) + fox(A43, B31) + fox(A44, B41)
    C42 = fox(A42, B22) + fox(A43, B32) + fox(A44, B42) + fox(A41, B12)
    C43 = fox(A43, B33) + fox(A44, B43) + fox(A41, B13) + fox(A42, B23)
    C44 = fox(A44, B44) + fox(A41, B14) + fox(A42, B24) + fox(A43, B34)

    return combine_matrix(C11, C12, C13, C14, C21, C22, C23, C24, C31, C32, C33, C34, C41, C42, C43, C44)

@pair_timing_decorator
def execute_fox(A, B):
    return fox(A, B)
        



    
        