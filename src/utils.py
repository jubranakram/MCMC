import numpy as np

'''
Utilities for Monte Carlo methods
Python code by: jubran akram
'''

def gaussian(x: float, mu: float=0, std: float=1/np.sqrt(2)):
    '''Calculates the gaussian function for the input x '''
    return np.exp(- 0.5* ((x - mu)/std)**2) / np.sqrt(2*np.pi*std*std)

def linear_congruential_generator(upper_lim, lower_lim, N: int, seed: int = 0):
    '''Generates N pseudorandom numbers between 0 and M-1'''

    x_0 = seed
    a, b = 123451121, 3456711
    M = 2**31
    nums = []
    for idx in range(1, N):        
        nums.append((a*x_0 + b) % M)
        x_0 = nums[idx-1]

    nums_in_interval = [(upper_lim - lower_lim) * n / (M - 1) + lower_lim for n in nums]

    return nums_in_interval

def pi_monte_carlo(N: int):
    '''Calculates pi using Monte Carlo simulation'''    
    
    r = (np.random.uniform(0, 1, size=(2, N))**2).sum(axis=0) < 1
    
    return 4*(r.sum()/N)

def integral_with_uniform_random_numbers(f, N:int, a:float = 0, b:float = 1):
    '''Calculates integral using uniform random numbers'''
    
    r = (b-a)*(f(np.random.uniform(a, b, size=N)).mean())
    
    return r

        



