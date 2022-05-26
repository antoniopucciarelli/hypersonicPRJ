# VARIABLES COMPUTATION -- needed as input for the final simulation
# importing libraries
import numpy as np 

# input variables -- molecular species: Argon  
M  = 25         # Mach number               [-]
Kn = 0.25       # Knudsen number            [-]
kb = 1.38e-23   # Boltzmann constant        [J/K]
T  = 200        # thermodynamic temperature [K]
m  = 6.63e-26   # Argon molecular mass      [kg]
d  = 4.17e-10   # Argon particle diameter   [m]
L  = 2          # reference length          [m] 
Wp = 1e+4       # 

# computing numberDensity and average molecular speed 

# speed of sound computation
c = np.sqrt((8 * kb * T) / (np.pi * m))

# average molecular speed computation
U = M * c 

# mean free path computation
lam = Kn * L 

# number density 
nrho = 1 / (lam * np.pi * d**2)

# mean free time computation
tau = lam / np.abs(U)

# number of simulated particles 
nsim = nrho / Wp

# printing results
starLen = 25
print('*'*starLen)
print('M      = {0:>10.2f}'.format(M))
print('Kn     = {0:>10.2f}'.format(Kn))
print('Wp     = {0:>10.3e}'.format(Wp))
print('kb     = {0:>10.3e} J/K'.format(kb))
print('T      = {0:>10.2f} K'.format(T))
print('m      = {0:>10.3e} kg'.format(m))
print('d      = {0:>10.3e} m'.format(d))
print('L      = {0:>10.2f} m'.format(L))
print('c      = {0:>10.2f} m/s'.format(c))
print('U      = {0:>10.2f} m/s'.format(U))
print('lambda = {0:>10.2f} m'.format(lam))
print('nrho   = {0:>10.3e} m-3'.format(nrho))
print('nsim   = {0:>10.3e} m-3'.format(nsim))
print('tau    = {0:>10.3e} s'.format(tau))
print('*'*starLen)
