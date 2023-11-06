import numpy as np
import sys
sys.path.append(r"C:/Users/Harrison/Desktop/Sg2023/Semaster 1/CEG 5201 hardware/CA announce/ceg5201_ca2")
from utils.time_consume import pair_timing_decorator
from multiprocessing import Pool, cpu_count
from utils.matrix_operations import split_matrix_4
from multiprocess import freeze_support
from matricx_multiply_algorithms.fox.fox import fox,combine_matrix
from utils.time_consume import group_timing_decorator, total_timing_decorator
def parallel_fox(args):
    return fox_multiprocessing(args[0], args[1], args[2])

def matrix_add(*matrices):
    result = matrices[0]
    for matrix in matrices[1:]:
        result += matrix
    return result

def fox_multiprocessing(A, B, depth=0, max_depth=1):
    if A.shape[0] <= 4 or B.shape[0] <= 4:
        return A @ B
    A11, A12, A13, A14, A21, A22, A23, A24, A31, A32, A33, A34, A41, A42, A43, A44 = split_matrix_4(A)
    B11, B12, B13, B14, B21, B22, B23, B24, B31, B32, B33, B34, B41, B42, B43, B44 = split_matrix_4(B)
    C11 = [[A11, B11], [A12, B21], [A13, B31], [A14, B41]]
    C12 = [[A12, B22], [A13, B32], [A14, B42], [A11, B12]]
    C13 = [[A13, B33], [A14, B43], [A11, B13], [A12, B23]]
    C14 = [[A14, B44], [A11, B14], [A12, B24], [A13, B34]]
    C21 = [[A21, B11], [A22, B21], [A23, B31], [A24, B41]]
    C22 = [[A22, B22], [A23, B32], [A24, B42], [A21, B12]]
    C23 = [[A23, B33], [A24, B43], [A21, B13], [A22, B23]]
    C24 = [[A24, B44], [A21, B14], [A22, B24], [A23, B34]]
    C31 = [[A31, B11], [A32, B21], [A33, B31], [A34, B41]]
    C32 = [[A32, B22], [A33, B32], [A34, B42], [A31, B12]]
    C33 = [[A33, B33], [A34, B43], [A31, B13], [A32, B23]]
    C34 = [[A34, B44], [A31, B14], [A32, B24], [A33, B34]]
    C41 = [[A41, B11], [A42, B21], [A43, B31], [A44, B41]]
    C42 = [[A42, B22], [A43, B32], [A44, B42], [A41, B12]]
    C43 = [[A43, B33], [A44, B43], [A41, B13], [A42, B23]]
    C44 = [[A44, B44], [A41, B14], [A42, B24], [A43, B34]]

    tasks = C11 + C12 + C13 + C14 + C21 + C22 + C23 + C24 + C31 + C32 + C33 + C34 + C41 + C42 + C43 + C44

    with Pool(processes = cpu_count()) as pool:
        results = pool.starmap(fox, tasks)
    C_sub = []
    for i in range(0, len(results), 4):
        C_sub.append(matrix_add(*results[i:i+4]))
    C = combine_matrix(*C_sub)
    return C

@pair_timing_decorator
def execute_fox_multiprocessing(A, B):
    return fox_multiprocessing(A, B)


if __name__ == '__main__':
    A = np.random.rand(16, 16)
    B = np.random.rand(16, 16)
    C = execute_fox_multiprocessing(A, B)

    assert np.allclose(C, A @ B)
    print("fox is right!")