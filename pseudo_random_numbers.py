import numpy as np
import matplotlib.pyplot as plt
from src.utils import linear_congruential_generator

'''
Generate N pseudorandom numbers using linear congruential generator between 0 and M-1
'''

if __name__ == "__main__":
    N = 10000
    M = 2
    # upper and lower limit
    u, l = 1, 0
    seed = 10
    nums = linear_congruential_generator(u, l, N, seed)
    num_bins = 20
    plt.figure()
    plt.hist(nums, bins=num_bins, edgecolor='k', alpha=0.5)
    plt.grid()
    plt.xlabel('$x$')
    plt.ylabel('Frequency')
    # plt.legend()
    plt.show()