import numpy as np
import matplotlib.pyplot as plt

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
    # sum the height
    z = np.sqrt(1 - r_squared[r_idx]).sum()

    print(f'The expectation value: {z/r_idx.sum()*2*np.pi}')
    print(f'Volume of a sphere: {np.pi*4/3}')