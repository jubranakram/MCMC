import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

'''
Calculate the volume of a ball defined by x**2 + y**2 + z**2 <= 1
Python code: jubran akram
'''

if __name__ == "__main__":
    # generate uniform random numbers
    N = 100000
    r = np.random.uniform(0, 1, size=(2, N))
    # square and sum 
    r_squared = (r**2).sum(axis=0)
    # check if x**2 + y**2 < 1 is met
    r_idx = r_squared < 1
    # sum the height z = sqrt(1 - x**2 - y**2)
    z = np.sqrt(1 - r_squared[r_idx])
    z_sum = z.sum()

    print(f'The expectation value: {z_sum/r_idx.sum()*2*np.pi}')
    print(f'Volume of a sphere: {np.pi*4/3}')

    ax = plt.axes(projection ="3d")

    ax.scatter3D(r[0, r_idx], r[1, r_idx], z, color = "green", alpha=0.1)
    ax.set_xlabel('$x$')
    ax.set_ylabel('$y$')
    ax.set_zlabel('$z$')
    ax.grid()
    
    
    # show plot
    plt.show()