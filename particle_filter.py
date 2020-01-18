# This function computes one iteration of the Particle Filter(Generic or Regularized)
# Given the state estimate xhat(k), covariance matrix, nonlinear
# measurement and dynamics models, and noise covariance matrices, computes
# the estimate xhat(k+1). This is the implementation of the Particle
# Filter.
# This function performs the Particle Filter state estimate for the
# dynamic system model
#
#   x(k+1) = f(k, x(k), u(k), v(k))
#   z(k+1) = h(k+1, x(k+1)) + w(k+1)
#
# Where v(k) and w(k+1) are Gaussian distributed random noise terms. The
# process noise v(k) has a mean of zero, and a Covariance Q(k). The
# measurement noise w(k+1) has a mean of zero, and a Covariance of R(k+1).
#
# Variables ending in "kp1" represent the variable at the(k+1) state.
# Variables ending in "k" represent variable at the(k) state.
#
# DEPENDENCIES: estimationModels.py
#               
# author: Man Jun Koh
# date: 4/16/2019
#
#

from estimationModels import dynamics_model, measurement_model
import numpy as np
from numpy.random import randn, uniform

def resample(chikp1mat,wkp1,Ns,Nx):
    
    # construct the CDF, c0 is zero
    cVec = np.zeros((Ns,1))
    for i in range(1,Ns):
        cVec[i,0] = cVec[i-1,0] + wkp1[i,:]
    
    # draw starting point - sample eta from uniform distribution 
    oneOverNs = 1/Ns
    eta1 = oneOverNs * uniform(0,1)
    
    # For each eta(j), find i such that c(i) <= eta(j) < c(i+1)
    chikp1matNew = np.zeros((Ns,Nx))
    jVec = np.zeros((Ns,1))
    
    # move along the cdf 
    for j in range(0,Ns):
        etaj = eta1 + j * oneOverNs
        i = 0
        while etaj > cVec[i,0] and i < Ns-1:
            i = i+1
        
        jVec[j,0] = i
        chikp1matNew[j,:] = chikp1mat[i,:].copy() 
    
    # normalize the weights again
    chikp1mat = chikp1matNew.copy()
    wkp1 = oneOverNs * np.ones((Ns,1))

    return chikp1mat, wkp1
    



def particle_filter(data):#xhat0, P0, Q, R, Ns):

    # extract the variables from the data dict 
    k = data['current time step']               # int 
    Ns = data['number of particles']            # int
    xhatk = data['state estimation']            # nx x 1
    #zkhist = data['measurement']                # nz x 1
    Pk = data['error covariance']               # nx x nx 
    Qk = data['process noise covariance']       # nv x nv
    zkp1 = data['next measurement']             # nz x 1
    Rk = data['measurement noise covariance']   # nz x nz 
    chikmat = data['particle matrix']           # Ns x Nx 
    wk = data['particle weight']                # Ns x 1
    Nt = data['resample threshold']             # int 

    # obtain the variable sizes
    Nx = 1#len(xhatk)
    Nz = 1#len(zkp1)
    Nv = 1#len(Qk)

    # initialize the filter if time step (k) is at 0 other wise skip
    if k == 0: 
        # obtain square root of covariance by taking cholesky factorization 
        if np.ndim(Pk) == 0:
            Sxk = np.sqrt(Pk)
        else:
            Sxk = np.linalg.cholesky(Pk)
        
        chikmat = xhatk + Sxk*randn(Ns,Nx)
        wk = (1/Ns) * np.ones((Ns,1))

    # compute square roots of covariance 
    if np.ndim(Qk) == 0:
        Svk = np.sqrt(Qk)
        invRkp1 = 1/Rk
    else:
        Svk = np.linalg.cholesky(Qk)
        invRkp1 = np.linalg.inv(Rk)

    # generate particles for process noise covariance 
    vkmat = Svk * randn(Ns,Nv)

    # particle propagation 
    chikp1mat = np.zeros((Ns,Nx))
    Zkp1mat = np.zeros((Ns,Nz))
    logwbarkp1 = np.zeros((Ns,1))
    logwk = np.log(wk)

    for i in range(0,Ns):
        # measurement prediction for particles 
        chikp1mat[i,:], _, _ = dynamics_model(chikmat[i,:],vkmat[i,:],k)
        Zkp1i,_ = measurement_model(chikp1mat[i,:],Rk,k+1)
        Zkp1mat[i,:] = Zkp1i

        # compute natural log of weights 
        nukp1i = zkp1 - Zkp1i
        logwbarkp1[i,:] = logwk[i,:] - 0.5 * np.transpose(nukp1i)*invRkp1*nukp1i

    # normalize the weights 
    logWbarMax = np.amax(logwbarkp1)
    wDoubleBarKp1 = np.exp(logwbarkp1-logWbarMax)
    sumWDoulbeBar = np.sum(wDoubleBarKp1)
    oneOverSumWDoubleBar = 1 / sumWDoulbeBar
    wkp1 = oneOverSumWDoubleBar * wDoubleBarKp1

    # update state estimation
    wkp1TimesChikp1 = np.multiply(wkp1,chikp1mat) 
    xhatkp1 = np.sum(wkp1TimesChikp1)

    # update A Posteriori Error Covariance
    chikp1MinusxhatMat = chikp1mat - xhatkp1
    Pkp1 = np.zeros((Nx,Nx))

    for i in range(0,Ns):
        Pkp1 = Pkp1 + wkp1[i,:] * chikp1MinusxhatMat[i,:] * np.transpose(chikp1MinusxhatMat[i,:])

    # Resample if degeneracy (N_eff < Nt occurs)
    wkp1Squared = np.square(wkp1)
    Neff = np.sum(wkp1Squared)
    if Neff < Nt: 
        chikp1mat,wkp1 = resample(chikp1mat,wkp1,Ns,Nx)

    
    return xhatkp1, Pkp1, chikp1mat, wkp1

