import numpy as np
from math import *
import matplotlib.pyplot as plt
import cmath

def geometry(I, J, rho0):
    rho = np.zeros((I, J))
    
    j_min = int(0.25 * (J-1))
    j_max = int(0.75 * (J-1))
    
    i_pos = int(0.4 * (I-1))
    rho[i_pos, j_min:j_max+1] = rho0
    
    i_neg = int(0.6 * (I-1))
    rho[i_neg, j_min:j_max+1] = -rho0
    
    return rho

def Dirichlet(I, J):
    N = I * J
    A = np.zeros((N, N))
    
    dx = 1.0/(I - 1)
    dy = 1.0/(J - 1)
    ex = 1.0/dx**2 
    ey = 1.0/dy**2  
    
    diagonal = -2 * (ex + ey)

    for i in range(I):
        for j in range(J):
            k = i * J + j  
            
            A[k, k] = diagonal
            
            if j > 0:
                A[k, k-1] = ex
            if j < J-1:
                A[k, k+1] = ex
            if i > 0:
                A[k, k-J] = ey
            if i < I-1:
                A[k, k+J] = ey
                
    return A

Nx, Ny = 65,65
E = Dirichlet(Nx, Ny)
rho = geometry(Nx, Ny, 1).flatten()

u = np.linalg.solve(E, -rho)

u2d = u.reshape(Nx, Ny)
plt.imshow(u2d, interpolation='bilinear', cmap='inferno', extent=[0, 1, 1, 0])
plt.colorbar()
plt.gca().invert_yaxis()
plt.title('Solution avec np.linalg.solve()')
plt.xlabel('x')
plt.ylabel('y')
plt.show()