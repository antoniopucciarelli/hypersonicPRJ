# VARIABLES COMPUTATION -- needed as input for the final simulation
# importing libraries
import numpy as np 

# input variables -- molecular species: Argon  
M  = 25         # Mach number                                       [-]
Kn = 0.25       # Knudsen number                                    [-]
kb = 1.38e-23   # Boltzmann constant                                [J/K]
T  = 200        # thermodynamic temperature                         [K]
m  = 6.63e-26   # Argon molecular mass                              [kg]
d  = 4.17e-10   # Argon particle diameter                           [m]
L  = 2          # reference length                                  [m] 
Wp = 1e+4       # weight factor                                     [-]
gamma = 5/3     # specific heat ratio                               [-]
Nlam  = 4       # number of mean free path dimension of the cell    [-]
Ntau  = 4       # number of time scale collision for the timestep   [-]
Ncell = 20      # number of particles that occupy each cell         [-]
Lx    = 10      # x direction domain dimension                      [m]
Ly    = 5       # y direction domain dimension                      [m]

# computing free stream properties
# speed of sound computation
cFS = np.sqrt((gamma * kb * T) / m)

# average molecular speed computation
U = M * cFS 

# mean free path computation
lamFS = Kn * L 

# number density 
nrhoFS = 1 / (lamFS * np.pi * d**2)

# mean free time computation
tauFS = lamFS / np.abs(U)

# number of simulated particles 
nsimFS = nrhoFS / Wp

# computing post shock properties 
# computing number density 
nrhoPS = (gamma + 1)/(gamma - 1) * nrhoFS

# computing number of simulated particles
nsimPS = nrhoPS / Wp

# computing translational temperature
TPS = nrhoFS/nrhoPS * U**2 / (3 * kb / m) 

# computing mean free path 
lamPS = 1 / (np.sqrt(2) * nrhoPS * np.pi * d**2)

# computing thermal velocity 
UthPS = np.sqrt(((8 * kb * TPS) / (np.pi * m)))

# computing collision time scale 
tauPS = 1 / (nrhoPS * np.pi * d**2 * UthPS)

# computing grid properties 
# cell size dimension
ds = lamPS / Nlam

# time step interval 
dt = tauPS / Ntau

# number cell computation
NxCells = np.int16(Lx / ds)
NyCells = np.int16(Ly / ds)

# printing results
starLen = 25
print('*'*starLen)
print('FREE STREAM PROPERTIES:')
print('M      = {0:>10.2f}'.format(M))
print('Kn     = {0:>10.2f}'.format(Kn))
print('gamma  = {0:>10.2f}'.format(gamma))
print('Wp     = {0:>10.3e}'.format(Wp))
print('kb     = {0:>10.3e} J/K'.format(kb))
print('T      = {0:>10.2f} K'.format(T))
print('m      = {0:>10.3e} kg'.format(m))
print('d      = {0:>10.3e} m'.format(d))
print('L      = {0:>10.2f} m'.format(L))
print('c      = {0:>10.2f} m/s'.format(cFS))
print('U      = {0:>10.2f} m/s'.format(U))
print('lambda = {0:>10.3e} m'.format(lamFS))
print('nrho   = {0:>10.3e} m-3'.format(nrhoFS))
print('nsim   = {0:>10.3e} m-3'.format(nsimFS))
print('tau    = {0:>10.3e} s'.format(tauFS))
print('\nPOST SHOCK PROPERTIES:')
print('nrho   = {0:>10.3e} m-3'.format(nrhoPS))
print('nsim   = {0:>10.3e} m-3'.format(nsimPS))
print('T      = {0:>10.2f} K'.format(TPS))
print('U      = {0:>10.2f} m/s'.format(UthPS))
print('lambda = {0:>10.3e} m'.format(lamPS))
print('tau    = {0:>10.3e} s'.format(tauPS))
print('\nGRID PROPERTIES:')
print('NxCells  = {0:>10d}'.format(NxCells))
print('NyCells  = {0:>10d}'.format(NyCells))
print('timeStep = {0:>10.3e} s'.format(dt))
print('*'*starLen)