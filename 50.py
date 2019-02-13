import matplotlib.pyplot as plt
import math
import numpy as np
t=np.arange(0,10,1)
s=t
plt.stem(t,s)
y=s
z=input('enter number')
i=0
s=0
for i in range (int(z)):
		s=s+y[i]
print (s)
plt.show()

