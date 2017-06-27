import numpy as np
import matplotlib.pyplot as plt


def working_with_text(title):
    np.random.seed(19680801)

    mu, sigma = 100, 15
    x = mu + sigma * np.random.randn(10000)

    #the histogram of the data
    n, bins, patches = plt.hist(x, 50, normed=1, facecolor='b',alpha=0.75)


    plt.xlabel('Smarts', fontsize=14, color='red')
    plt.ylabel('Probabality', fontsize=12, color='green')
    plt.title(title)
    plt.text(60, .025, r'$\mu_i=100,\ \sigma_2=15$')
    plt.axis([40, 160, 0, 0.03])
    plt.grid(True)
    plt.show()
    plt.close()


working_with_text('Histogram of IQ')

