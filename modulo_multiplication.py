# -*- coding: utf-8 -*-
"""
Created on Mon Jul 26 15:20:56 2021

Multiplication tables.

@author: Filip Becanovic
"""


import numpy as np
from matplotlib import pyplot as plt

def multiplication_table(n, p):
    """
    Modular multiplication table.

    Parameters
    ----------
    n : integer
        The value of the modulo, otherwise the number of elements.
    p : integer
        The number with which we multiply.

    Returns
    -------
    A list of output values for the multiplication in order.

    """
    return [(i * p) % n for i in range(n)]


def plot_modular_mapping(m):
    """
    Plots the modular mapping on a circle.

    Parameters
    ----------
    m : list of integers
        This is a list of outputs of modular mappings of length n. Meaning that
        the i-th element is a mapping from integer i to m[i].

    Returns
    -------
    None.

    """
    # Extract constants
    n = len(m)
    
    # Each number
    wn = np.exp(1j * 2 * np.pi * np.arange(n) / n)
    
    # Get a full circle
    t = 1000
    wt = np.exp(1j * 2 * np.pi * np.arange(t) / t)
    
    # Each number
    wn = np.exp(1j * 2 * np.pi * np.arange(n) / n)
    
    # Plot
    fig = plt.figure(figsize=(12.8, 7.2))
    
    plt.plot(wt.real, wt.imag, 'k', label = '_nolegend_')
    plt.plot(wn.real, wn.imag, 'ro')
    for i in range(n):
        plt.text(1.1*wn[i].real, 1.1*wn[i].imag, str(i), ha='center', va='center')
    for i in range(n):
        x = [wn[i].real, wn[m[i]].real]
        y = [wn[i].imag, wn[m[i]].imag]
        plt.plot(x, y, 'k', label = '_nolegend_')
    plt.axis('square')
    ax = plt.gca()
    ax.axes.xaxis.set_visible(False)
    ax.axes.yaxis.set_visible(False)
    ax.axis('off')
    
    
# %% 

# Define numbers
n = 100
p = 10

# Get the multiplication table
m = multiplication_table(n, p)

# Plot and title
plot_modular_mapping(m)
plt.title('Multiplication table of %d modulo %d' % (p, n), fontsize=20)