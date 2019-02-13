import scipy.io.wavfile as wav
import numpy as np
from matplotlib import pyplot as plt
def mean(lst): return sum(lst)/len(lst)
fs,g=wav.read('uday1.wav')
t=np.arange(0,len(g)/fs,1.0/fs)
noise=np.random.normal(0,10,g.shape)
plt.subplot(411)
plt.title('sin wave')
plt.plot(t,g)
a=list([g])
noise1=g+noise
plt.subplot(412)
plt.title('noise')
plt.plot(noise)
plt.subplot(413)
plt.title('noise sin')
g=abs(g)
env=np.zeros_like(g)
for i in range(len(g)):
		env[i]=mean(g[max(i-1000,0):i+1])
plt.subplot(414)
plt.title('mean avg')
plt.plot(range(len(g)))
plt.show()
#g=noise
