# this function simulates true values for both dynamics and
# measurement model time history
#
# author: Man Jun Koh
# Date: 4/1/2019 
# 
#

from estimationModels import dynamics_model, measurement_model
import numpy as np
from numpy.random import randn  

def tru_simulation(xhat0,P0,Q,R,Ns):

    # initialize the variables 
    vkhist = np.sqrt(Q)*randn(Ns,1)
    xkhist = np.zeros((Ns+1,1))
    zkhist = randn(Ns,1)
    zkhist_zeronoise = np.zeros((Ns,1))

    xkhist[0,0] = xhat0 + np.sqrt(P0)*randn(1,1)

    for k in range(0,Ns-1):
        kp1 = k + 1

        # compute each model 
        xkhist[kp1,0], _, _ = dynamics_model(xkhist[k, :], vkhist[k, :], k)
        zkperfect, _ = measurement_model(xkhist[k, :],R,k)

        # update the measurement model 
        zkhist[k,:] = zkperfect + zkhist[k,:]
        zkhist_zeronoise[k,:] = zkperfect

    return xkhist, zkhist

#xtru, ztru= tru_simulation(4,2,1,0.25,10)
#print(xtru)
#print(ztru)



