import numpy as np
import matplotlib.pyplot as plt
from src.utils import integral_with_uniform_random_numbers

'''
Solve an integral aSb f(x) dx using Monte Carlo simulations
Python code by: jubran akram
'''

def f(x):
    return np.sqrt(1 - x*x)

if __name__ == "__main__":
    num_realizations = [10, 100, 1000, 10000, 100000, 1000000]    
    a, b = 0, 1
    results = [integral_with_uniform_random_numbers(f, num, a, b) for num in num_realizations]

    plt.semilogx(num_realizations, results, 's--k', linewidth=2, alpha=0.5, label='Calculated')
    plt.semilogx(num_realizations, np.pi/4*np.ones((len(num_realizations),)), 'b', alpha=0.5, linewidth=2, label='True')
    plt.grid()
    plt.xlabel('# of realizations')
    plt.ylabel('$\\frac{\pi}{4}$ value')
    plt.show()