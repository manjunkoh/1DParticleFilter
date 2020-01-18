# This script computes the dynamics model f at time step k using 
# the state xk and process noise vk and masurement model h at time 
# step k using state xk, and measurement noise Rk.
#
# author: Man Jun Koh
# Date: 4/1/2019 
#
#

import numpy as np

# compute f the dynamics model and the jacobian matricies 
def dynamics_model(xk,vk,k):

    atanxk = np.arctan(xk)
    pi = np.pi
    f = 2*atanxk + 0.5*np.cos(pi*k/3) + vk

    dfdx = 2/(1+(xk**2))
    dfdv = 1

    return f,dfdx,dfdv

# compute h the measurement model and the jacobian matricies 
def measurement_model(xk,Rk,k):

    oneoversqrtRk = 1/np.sqrt(Rk)
    
    h = oneoversqrtRk * (xk**3 + xk**2 + xk)
    dhdx = oneoversqrtRk * (3*xk**2 + 2*xk)

    return h,dhdx






