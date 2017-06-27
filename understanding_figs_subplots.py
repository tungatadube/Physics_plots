import matplotlib.pyplot as plt
import numpy as np


def understand_figs(title):
    plt.figure(1)   # the first figure
    plt.subplot(211) # the first subplot in the first figure
    plt.plot([1, 2, 3])
    plt.subplot(212) # the second subplot in the first figure
    plt.plot([4, 5, 6])

    plt.figure(2)    # a second figure
    plt.plot([4, 5, 6]) # creates a subplot (111) by default

    plt.figure(1) # make figure 1 current, subplot(212) still current
    plt.subplot(211) # make subplot(211) in figure 1 current
    plt.title(title) #subplot 211 title
    plt.show()
    plt.clf()
    plt.close()

understand_figs('This is my subplot')








