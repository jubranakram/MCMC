import matplotlib.pyplot as plt
import numpy as np
from src.utils import gaussian
'''
Gaussian function
Python code by: jubran akram
'''
if __name__ == "__main__":

    x = np.linspace(-5, 5, 100)
    g = gaussian(x)

    plt.plot(x, g, 'k', linewidth=2, alpha=0.5)
    plt.grid()
    plt.xlabel('$x$')
    plt.ylabel('$P(x)$')


    # with mean and standard deviation values
    
    plt.figure()
    sigma = [1, 2, 3]
    colors = ['k', 'b', 'r']
    for s, c in zip(sigma, colors):
        g = gaussian(x, 0, s)
        plt.plot(x, g, c, linewidth=2, alpha=0.5, label=f'$\sigma={s}$')
    plt.grid()
    plt.xlabel('$x$')
    plt.ylabel('$P(x)$')
    plt.legend()

    plt.show()