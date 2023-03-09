import numpy as np
import matplotlib.pyplot as plt
from src.utils import pi_monte_carlo

'''
Calculate the value of pi using uniform random numbers (Monte Carlo simulation)
Python code by: jubran akram
'''

if __name__ == "__main__":
    num_realizations = [10, 100, 1000, 10000, 100000, 1000000]
    pi_values = [pi_monte_carlo(num) for num in num_realizations]

    plt.semilogx(num_realizations, pi_values, 's--k', linewidth=2, alpha=0.5, label='Calculated')
    plt.semilogx(num_realizations, np.pi*np.ones((len(num_realizations),)), 'b', alpha=0.5, linewidth=2, label='True')
    plt.grid()
    plt.xlabel('# of realizations')
    plt.ylabel('$\pi$ value')
    plt.show()