import numpy as np
import matplotlib.pyplot as plt

#Annotating text

ax = plt.subplot(111)

t = np.arange(0.0, 5.0, 0.01)
s = np.cos(2*np.pi*t)
line, = plt.plot(t, s, lw=2)

plt.annotate('local max', xy=(2, 1), xytext=(1.5, 1.5), arrowprops=dict(facecolor='brown', shrink=0.05),)
plt.annotate('local min', xy=(2.5,-1), xytext =(3,-1.5), arrowprops=dict(facecolor='grey', shrink=0.05), )
x = np.linspace(0,5 ,6)
y= 0 + 0*x
plt.plot(x,y, lw=0.5, color='red')
plt.ylim(-2,2)
plt.show()
plt.close()