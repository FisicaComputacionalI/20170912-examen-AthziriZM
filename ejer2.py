import numpy as np
import matplotlib.pyplot as plt
def f(t):
    return 2*np.sin(2*np.pi*t)+2015
t=np.arange(0.0,10,0.2)
plt.figure(1)
plt.plot(t, 2*np.sin(2*np.pi*t)+2015, 'r--')
plt.savefig('Univesidad.png')
plt.show()
