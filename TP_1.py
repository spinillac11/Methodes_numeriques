from mpmath import *
import numpy as np
import matplotlib.pyplot as plt

###### Ej1
# mp.dps = Nmax
# print(mp.pi)
# x = mpf(10**9.)
# n = Nmax0

# while (x + 2**(-n)) == x:
#     n = n-1
# print(f"for precision {mp.dps}, x = {x}, nmin = {n}" )

###### Ej2

# sum1 = 0
# sum2 = 0
# n = 1

# while np.abs(sum1 - sum2) < 1:
#     a = np.pow(10., n)
#     b = -np.pow(10., n)
#     c = 1
#     sum1 = (a + b) + c
#     sum2 = a + (b + c)
#     n = n + 1

# print(n)
# print(sum1)
# print(sum2)


###### Ej3

# x1_1 = 0
# x1_2 = 0
# n = 1

# while (x1_1 - x1_2) < 1:
#     pown_ = np.pow(10., -n)
#     pow = np.pow(10., n)

#     x2_1 = (0.5 - pown_)/(1 - pown_)
#     x1_1 = 1 - x2_1

#     x2_2 = (1 - 0.5*pow)/(1 - pow)
#     x1_2 = 1 - x2_2
#     n += 1

# print(n)
# print(x1_1)
# print(x1_2)

###### Ej4

def factorial(n):
    if n <= 0:
        return 1
    return n*factorial(n-1)

def sum(x, n_data):
    sum = 0.0
    for ii in range(0, n_data):
        sum += np.pow(-1.0, ii)*np.pow(x, 2.0*ii)/factorial(2.0*ii)
    return sum

def recursive(x, n_data):
    term = 1.0
    sum = 0.0
    for ii in range(0, n_data):
        term *= -np.pow(x, 2)/(np.pow(2.*ii, 2)+6*ii+2) # cette calcule ne depend pas de n
        sum += term
    return sum

Nmax = 15

sol_fac = np.zeros(Nmax)
sol_recursive = np.zeros(Nmax)
x = 3
for n in range (0, Nmax):
    sol_fac[n] = sum(x, n)
    sol_recursive[n] = recursive(x, n)

n = np.arange(0, Nmax, 1)
plt.figure()
plt.plot(sol_fac, label = "Sol primitive")
plt.plot(sol_recursive, label = "Sol recursive")
plt.axhline(np.cos(x))
plt.legend()
plt.show()