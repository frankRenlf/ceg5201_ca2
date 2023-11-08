# -*- coding: UTF-8 -*-
"""
    @Author : Frank.Ren
    @Project : ceg5201_ca2 
    @Product : PyCharm
    @createTime : 2023/11/8 20:55 
    @Email : e1143935@u.nus.edu
    @github : https://github.com/frankRenlf
    @Description : draw the speedup plot
"""


def speedup_plot(speedups, labels, path, filename="speedup_plot.png"):
    import matplotlib.pyplot as plt
    import numpy as np

    if not isinstance(speedups[0], list):
        speedups = [speedups]

    x = np.arange(1, len(speedups[0]) + 1)
    for i, speedup in enumerate(speedups):
        plt.plot(x, speedup, 'o-', label=labels[i])

    plt.xlabel("Number of Processes")
    plt.ylabel("Speedup")
    plt.title("Speedup for processes in Strassen's Algorithm")
    plt.legend(loc='best')
    plt.savefig(path + filename, dpi=300)

    # 现在展示图像
    plt.show()


def draw_g0(data, path):
    speedup = [data[0] / data[i] for i in range(0, len(data))]
    print(speedup)
    speedups = [speedup]
    labels = ['g0']
    speedup_plot(speedups, labels, path, filename="g0_speedup.png")


def draw_pair(data, path):
    speedups = [[data[i][0] / data[i][j] for j in range(0, len(data[i]) // 2)] for i in range(0, len(data))]
    labels = ['pair0', 'pair1', 'pair2', 'pair3', 'pair4', 'pair5', 'pair6', 'pair7']
    print(len(speedups))
    speedup_plot(speedups, labels, path, filename="pair_speedup.png")


def draw_cumulate(data, path):
    speedups = [[data[i][0] / data[i][j] for j in range(len(data[i]) // 2, len(data[i]))] for i in range(0, len(data))]
    labels = ['pair0-0', 'pair0-1', 'pair0-2', 'pair0-3', 'pair0-4', 'pair0-5', 'pair0-6', 'pair0-7==G0']
    print(len(speedups))
    speedup_plot(speedups, labels, path, filename="pair_cumulate_speedup.png")

# if __name__ == "__main__":
