import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return 2*np.sen(2*np.pi*t2)+2015
    return t+1997
t1=np.arange(0.0, 20, 0.1)
t2=np.arange(0.0, 10, 0.2)
plt.figure(1)
plt.subplot(211)
plt.plot(t1, t1+1997, 'bo')
plt.subplot(212)
plt.plot(t2, 2*np.sin(2*np.pi*t2)+2015, 'r--')
plt.savefig('Dosfunciones.png')
plt.show()
