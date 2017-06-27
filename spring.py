import matplotlib.pyplot as plt
import numpy as np

def spring_stiffness(title):

    '''
    The function plots an Extension to load graph for two springs that obey Ohm's law

    >>> E = F/K
    [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

    '''

    # generate values of the forces

    F = np.arange(100.0, 500.0, 50.0)
    k = 10
    E = F/k


    plt.figure(figsize = (8,6), dpi= 100,)
    plt.plot(E, F, linewidth = 1.5, linestyle = '-', color = 'blue', label = "Eric's spring")

    plt.xticks(np.arange(10.0, 50.0, 5.0))
    plt.yticks(np.arange(100, 500, 50))
   
    t = 100
    plt.scatter([t/k,], [t,], 30, color = 'blue')
    plt.plot([t/k, 45], [100, t], color='blue', linewidth=1.5, linestyle='--')
    #plt.annotate(r'$x_1=10, y_1=100$', xy=(t/k, t), xycoords='data', xytext=(+50, +100), textcoords='offset points', fontsize=12, arrowprops=dict(arrowstyle= '->', connectionstyle='arc3, rad=.2'))


    t = 450
    plt.scatter([t/k,], [t,], 30, color = 'blue')
    plt.plot([t/k,t/k],[100, t], color='blue', linewidth=1.5, linestyle='--')

    F = np.arange(100.0, 500.0, 50.0)
    k = 11
    E = F/k
    
    plt.xticks(np.arange(10.0, 50.0, 5.0))
    plt.yticks(np.arange(100, 500, 50))
    plt.plot(E, F, linewidth = 1.5, linestyle = '-', color = 'red', label = "Caroline's spring")

    t = 100
    plt.scatter([t/k,], [t,], 30, color = 'red')
    plt.plot([t/k, 40 ],[100, t], color='red', linewidth=1.5, linestyle='--')
    plt.plot([t/k, 45], [100, t], color='blue', linewidth=1.5, linestyle='--')
    plt.annotate(r'$x_1=23, y_1=100$', xy=(t/k, t), xycoords='data', xytext=(+50, +5), textcoords='offset points', fontsize=12, color='red', arrowprops=dict(arrowstyle= '->', connectionstyle='arc3, rad=.2', color='green'))


    t = 450
    plt.scatter([t/k,], [t,], 30, color = 'red')
    plt.plot([t/k,t/k],[100, t], color='red', linewidth=1.5, linestyle='--')
    plt.annotate(r'$x_2=40.9, y_2=450$', xy=(t/k, t), xycoords='data', xytext=(20, 400), fontsize=12, color= 'red', arrowprops=dict(arrowstyle= '->', connectionstyle='arc3, rad=.2', color='green'))
    
    
    plt.grid(linewidth=0.2, color='green',)



    plt.title(title, color='green')
    plt.ylabel('Force/N', color = 'green')
    plt.xlabel('Extension/mm', color = 'green')
    ax = plt.gca()
    ax.spines['right'].set_color('none')
    ax.spines['top'].set_color('none')
    plt.legend(loc= 'upper left', frameon = False, )


    plt.show()
    plt.close()

spring_stiffness('Force-Extension graph at Sihlengeni High')





