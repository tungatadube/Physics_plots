import numpy as np
import matplotlib.pyplot as plt

x = np.linspace(-np.pi, np.pi, 256, endpoint = True)
C, S = np.cos(x), np.sin(x)






plt.figure(figsize = (8,6), dpi = 100)
plt.subplot(111)
x = np.linspace(-np.pi, np.pi, 256, endpoint = True)
C, S = np.cos(x), np.sin(x)
plt.plot(x, C, color = 'blue', linewidth = 2.0, linestyle = '-', label = 'cosine')
plt.plot(x, S, color = 'red', linewidth = 3.0, linestyle = '-', label = 'sine')
plt.legend(loc='upper left', frameon=True)
# Set x_limits
plt.xlim(x.min()*1.1, x.max()*1.1)
 #Set y_lim
plt.ylim(C.min()*1.1, C.max()*1.1)

 #set yticks
plt.yticks([-1, 0, +1], [r'$-1$', r'$0$', r'$+1$'])
 #set xticks
plt.xticks([-np.pi, -np.pi/2, 0, np.pi/2, np.pi], [r'$-\pi$', r'$-\pi/2$', r'$0$', r'$+\pi/2$', r'$+\pi$'])

ax = plt.gca()
ax.spines['right'].set_color('none')
ax.spines['top'].set_color('none')
ax.xaxis.set_ticks_position('bottom')
ax.spines['bottom'].set_position(('data', 0))
ax.yaxis.set_ticks_position('left')
ax.spines['left'].set_position(('data', 0))



 #save figure using 72n dots per inch
plt.savefig('plot3.pdf', dpi = 720)

 #show results on screen
plt.show()
plt.close()

