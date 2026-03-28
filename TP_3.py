import numpy as np
import time
import matplotlib.pyplot as plt
from scipy.stats import linregress
import sympy as sp

######### Excercise 1 #################
Nmax = 1000

N = np.arange(100, Nmax, 10)
size = np.size(N)
t = np.zeros(size)
norm1 = np.zeros(size)  
norm2 = np.zeros(size)

print (size)

for i, n in enumerate(N):
    
    A = np.random.rand(n, n)
    b = np.random.rand(n)

    start = time.time()
    invA=np.linalg.inv(A)
    

    x1=invA@b
    x2=np.linalg.solve(A,b)
    end = time.time()
    t[i] = end - start
    delta1 = A@x1 - b
    delta2 = A@x2 - b
    norm1[i] = np.linalg.norm(delta1)
    norm2[i] = np.linalg.norm(delta1)

logN = np.log10(N)
logt = np.log10(t)

res = linregress(logN, logt)
m = res.slope
b = res.intercept


plt.figure()
plt.plot(logN, logt,  label = "logN Vs. logt" )
plt.plot(logN, [m*i+b for i in logN], label = f"Linear reg m = {m}")
plt.legend()
plt.show()
plt.close()

plt.figure()
plt.plot(N, norm1,  label = "Manual sol" )
plt.plot(N, norm2, label = "Linalg sol")
plt.legend()
plt.show()
plt.close()
   
######## Excercise 2 #################


# Nmax = 1000

# def Vandermonde(N):
#     start = time.time()
#     x_ref = np.linspace(-1, 1, N + 1)
#     # Cuadrature
#     q = np.array([(1** (k + 1) + (-1)** (k + 1)) / (k + 1) for k in range (N + 1)])
#     A = np.zeros((N + 1, N + 1))

#     x = sp.symbols('x')

#     for j in range (N + 1):
#         pj = 1
#         for n in range (N + 1):
#             if n != j:
#                 pj *= (x - x_ref[n])/(x_ref[j] - x_ref[n]) 

#         poly_pj = sp.Poly(pj, x)
#         Coeffs = poly_pj.all_coeffs()[::-1]

#         for k, c in enumerate(Coeffs):
#             A[j, k] = c

#     w = A@q

#     end = time.time()

#     X = np.vandermonde(N + 1)
#     err = X@w - q

#     time = end-start

#     return err, time
