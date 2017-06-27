import matplotlib.pyplot as plt
import numpy as np 


plt.figure(1)
plt.subplot(211)
plt.plot([1, 2, 3])
plt.subplot(212)
plt.plot([4, 5, 6])
plt.yticks(np.linspace(4,6,6, endpoint = True))
plt.show()

plt.figure(2)
plt.plot([4, 5, 6])

#plt.show()