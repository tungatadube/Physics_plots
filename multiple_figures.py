import numpy as np
import matplotlib.pyplot as plt


def f(t):
    return np.exp(-t)* np.cos(2*np.pi*t)

t1 = np.arange(0.0, 5.0, 0.1)
t2 = np.arange(0.0, 5.0, 0.02)

#The figure() command here is optional because figure(1) will be created by default, just as a
#subplot(111) will be created by default if you don’t manually specify any axes. The subplot() command specifies numrows, numcols, fignum where fignum ranges from 1 to numrows*numcols. The
#commas in the subplot command are optional if numrows*numcols<10. So subplot(211) is identical
#to subplot(2, 1, 1). You can create an arbitrary number of subplots and axes. If you want to place
#an axes manually, i.e., not on a rectangular grid, use the axes() command, which allows you to specify
#the location as axes([left, bottom, width, height]) where all values are in fractional (0 to 1) coordinates. See pylab_examples example code: axes_demo.py for an example of placing axes manually and
#pylab_examples example code: subplots_demo.py for an example with lots of subplots.

plt.figure(1)
plt.subplot(211)
plt.plot(t1,f(t1), 'bo', t2, f(t2), 'k')
plt.title('First subplot of fig 1')

plt.subplot(212)
plt.plot(t2, np.cos(2*np.pi*t2), 'r--')
plt.title('Second subplot in the second figure')
plt.show()
