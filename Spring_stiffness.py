import matplotlib.pyplot as plt
import numpy as np

def spring_stiffness(title):

    '''
    The function plots an Extension to load graph for two springs that obey Ohm's law

    >>> E = F/K
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    '''

    # generate values of the forces

    F = np.arange(0, 100, 10)
    k = 10
    E = F/k 


    plt.figure(figsize = (8,6), dpi= 100)
    plt.plot(E, F, linewidth = 2.5, linestyle = '-', color = 'blue', label = 'Spring 1')

    F = np.arange(0, 100, 10)
    k = 20
    E = F/k 
    plt.plot(E, F, linewidth = 2.5, linestyle = '-', color = 'red', label = 'Spring 2')

    plt.title(title, color='green')
    plt.ylabel('Force/N', color = 'green')
    plt.xlabel('Extension/cm', color = 'green')
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.legend(loc= 'upper left', frameon = False)

    plt.show()
    plt.close()

spring_stiffness('Force-Extension graph')





