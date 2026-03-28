import numpy as np
from scipy.fft import fft, fftfreq
from math import *
import matplotlib.pyplot as plt
import cmath

#alpha = 1.0
t0 = 25.0
fe = 20.0
t = np.arange(0, 50, 1/fe)
N = len(t)
fc = 1.0 
alpha = (np.pow(pi,2)/np.log(2))*np.pow((fc/2),2)

signal = np.exp(-alpha*(t0-t)**2)*np.sin(2*pi*fc*t)

plt.figure()
plt.plot(t, signal)
plt.show()

def FT (s):
    N = len(s)
    S = np.zeros(N, dtype=complex)

    for k in range(N):
        sum = 0
        for n in range(N):
            sum += s[n]*np.exp(2j*pi*n*k/N)
        S[k] = sum

    return S
    
def IFT (S):
    N = len(S)
    s = np.zeros(N, dtype=complex)

    for n in range(N):
        sum = 0
        for k in range(N):
            sum += S[k]*np.exp(-2j*pi*n*k/N)
        s[k] = sum

    return s

freqs = np.arange(N)*fe/N
Signal_tf = FT(signal)

plt.figure()
plt.plot(freqs, np.abs(Signal_tf))
plt.xlim(0, fe/2)
plt.show()

