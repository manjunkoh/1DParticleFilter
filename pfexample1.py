from tru_sim import tru_simulation
from particle_filter import particle_filter
import matplotlib.pyplot as plt 
import numpy as np
import time 


# begin timing to determine computation time 
start = time.time()

# intialize given variables 
Qk = 1
P0 = 2
Rk = 0.25
xhat0 = 4
K = 100
Ns = 500
Nx = 1
Nz = 1

# run the truth simulation for comparison in plots  
xkhist_tru, zkhist_tru =tru_simulation(xhat0,P0,Qk,Rk,K)

# initialize the variables before running the filter 
pfData = {}
pfData['current time step'] = 0                 # k
pfData['number of particles'] = Ns              # Ns
pfData['state estimation'] = xhat0              # xhatk, xhat0 first
pfData['error covariance'] = 2                  # Pk 
pfData['process noise covariance'] = 1          # Qk
pfData['next measurement'] = zkhist_tru[0,:]
pfData['measurement noise covariance'] = 0.25   # Rk
pfData['particle matrix'] = np.nan              # chi 
pfData['particle weight'] = np.nan              # wk
pfData['resample threshold'] = 40

xhathist = np.zeros((K,Nx))
Phist = np.zeros((Ns,Nx,Nx))
#kp1 = K + 1

# run the particle filter for each time step k
for k in range(0,K):

    kp1 = k + 1
    # pass in the current measurement 
    pfData['next measurement'] = zkhist_tru[k, :]
    xhatkp1, Pkp1, chikp1mat, wkp1 = particle_filter(pfData)

    # store the estimation
    xhathist[k,:] = xhatkp1
    Phist[k,:,:] = Pkp1

    # iterate 
    pfData['state estimation'] = xhatkp1
    pfData['error covariance'] = Pkp1
    pfData['particle matrix'] = chikp1mat
    pfData['particle weight'] = wkp1
    pfData['current time step'] = kp1



# set up the plot layout 
plt.figure(1)
plt.rcParams.update({'font.size': 35})
ax = plt.gca()
ax.tick_params(axis='both', which='major', labelsize=24)
plt.grid(True)

# plot the result 
plt.scatter(np.linspace(0, 100, 100), xkhist_tru[0:-1, 0],s=700, label = 'Truth State (xk)')
plt.scatter(np.linspace(0, 100, 100), xhathist[:, 0], marker = 'x', linewidth = 5,s=700, label = 'PF (Ns = 500, Nt = 40)')
plt.title('Truth State vs Particle Filter')
plt.xlabel('Time History (k)', fontsize=30)
plt.ylabel('System State (x)', fontsize=30)
plt.legend()
plt.show()

end = time.time()
print('computation time: ', end - start, 'seconds')
