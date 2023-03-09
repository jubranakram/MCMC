import numpy as np
import matplotlib.pyplot as plt

'''
Central limit theorem:

 Let's assume we have K sources of errors. Each source of error gives a uniform random number between
 -0.5 and +0.5. The total error is then the sum of K errors
'''

if __name__ == "__main__":
    num_realizations = 10000
    num_error_sources = 100
    errors = [np.random.uniform(-0.5, 0.5, size=100).sum() for _ in range(num_realizations)]
    errors = [e/np.sqrt(num_error_sources) for e in errors]
    num_bins = 20
    plt.figure()
    plt.hist(errors, bins=num_bins, density=1, edgecolor='k', alpha=0.5)
    plt.grid()
    plt.xlabel('$x$')
    plt.ylabel('$P(x)$')
    # plt.legend()
    plt.show()