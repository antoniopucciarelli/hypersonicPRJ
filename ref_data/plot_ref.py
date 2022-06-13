		#plot reference quantities for martian re-entry
import numpy as np
import matplotlib.pyplot as plt
from scipy import interpolate

data_rho = np.loadtxt('martian_rho.dat',
                     delimiter=',')
#altitude
data_h   = np.loadtxt('altitude_time.dat',
                     delimiter=';')
#valocity
data_v  = np.loadtxt('Descending_velocity.dat',
                     delimiter=';')
#temperature
data_T  = np.loadtxt('Temperature.dat',
                     delimiter=',')
#%% plot to check the extracted data

#density
plt.figure(1)
plt.semilogx(data_rho[:,0],data_rho[:,1])
plt.title("Martian density")
plt.xlabel("Density [kg/m3]")
plt.ylabel("Altitude [km]")
plt.show()

#Temperature
plt.figure(2)
plt.plot(data_T[:,0],data_T[:,1])
plt.title("Temperature altitude")
plt.xlabel("Temperature [K]")
plt.ylabel("Altitude [km]")
plt.show()

#altitude
plt.figure(3)
plt.plot(data_h[:,0],data_h[:,1])
plt.title("Altitude time")
plt.xlabel("Time [s]")
plt.ylabel("Altitude [km]")
plt.show()

#velocity
plt.figure(4)
plt.plot(data_v[:,0],data_v[:,1])
plt.title("Velocity time")
plt.xlabel("Time [s]")
plt.ylabel("Velocity [km/s]")
plt.show()

#range from -13 to 250 s -> interpolate this one
time_vect = np.linspace(2, 250, 1000)
#%% interpolating velocity and altitude
# velocity piecewise linear interpolation with time
f_v = interpolate.interp1d(data_v[:,0], data_v[:,1])
#evaluating the function in time_vect -> conversion in m/s
v_vect = f_v(time_vect)*1000 #converted in m/s
# the same is done for the altitude
f_h = interpolate.interp1d(data_h[:,0], data_h[:,1])
# vector h_vect
h_vect = f_h(time_vect)

# plot altitude velocity

plt.figure(5)
plt.plot(v_vect,h_vect)
plt.title("Velocity altitude")
plt.ylabel("Altitude [km]")
plt.xlabel("Velocity [m/s]")
plt.show()

# interpolating temperature and density over h_vect
f_rho    = interpolate.interp1d(data_rho[:,1], data_rho[:,0])
f_T      = interpolate.interp1d(data_T[:,1], data_T[:,0])

rho_vect = f_rho(h_vect)
T_vect   = f_T(h_vect)
#%% CHECK INTERPOLATION
#density
#plt.figure(6)
#plt.semilogx(rho_vect,h_vect)
#plt.title("CHECK Martian density")
#plt.xlabel("Density [kg/m3]")
#plt.ylabel("Altitude [km]")
#plt.show()

#Temperature
#plt.figure(8)
#plt.plot(T_vect,h_vect)
#plt.title("CHECK Temperature altitude")
#plt.xlabel("Temperature [K]")
#plt.ylabel("Altitude [km]")
#plt.show()

#%% COMPUTE KN AND MA VARYING DURING DESCENDING
#KN
L = 5 #m -> capsule diameter
#molecular masses and mass fraction
mmCO2 = 7.31E-26  #kg -> mass of just one molecule
mmN2  = 4.65E-26  #kg
#molecular weight amu
mwCO2 = 44.0      #amu -> mass of one mole
mwN2  = 28.016    #amu
#mass fraction
YCO2  = 0.97
YN2   = 0.03
#average diameter of particles
d = 4.1E-10

#gas nummber density(number of particles per m^3)
n_vect = rho_vect/(YCO2*mmCO2+YN2*mmN2)

mfp_vect = 1/(np.sqrt(2)*n_vect*np.pi*d**2)

#KN calculation
KN_vect  = mfp_vect/L

#plot KN variation in respect to altitude

plt.figure(9)
plt.semilogx(n_vect,h_vect)
plt.title("Number density")
plt.xlabel("n")
plt.ylabel("Altitude [km]")
plt.show()

plt.figure(10)
plt.plot(KN_vect,h_vect)
plt.title("KN")
plt.xlabel("KN")
plt.ylabel("Altitude [km]")
plt.show()
#MA computation

#equivalent R computation
kB = 1.380649e-23

RCO2 = kB/mmCO2 # already in SI units
RN2  = kB/mmN2

# equivalent gas constant for the mixture
R = YCO2*RCO2 + YN2*RN2

# gamma computation
#rotational degrees are active since very small T
#asyntotic condition -> T is high enough for activation of rotational dof not
#for vibrational ones
cvN2  = (3/2+1)*RN2   #sum of contribution of internal and rotational energy level
cvCO2 = (3/2 + 2)*RCO2 # each rotational 1/2*R -> CO2 is not bi-molecular
                       # so rotational energy level is higher

#mixture cv and cp
cv = YCO2*cvCO2 + YN2*cvN2
cp = YCO2*(RCO2+cvCO2) + YN2*(RN2+cvN2)

#computing gamma for the mixture
gamma = cp/cv

#computing speed of sound
c_vect = np.sqrt(gamma*R*T_vect)
#Mach number computation
Ma_vect = v_vect/c_vect

#plot Mach variation with altitude
plt.figure(11)
plt.plot(Ma_vect,h_vect)
plt.title("Ma")
plt.xlabel("Ma")
plt.ylabel("Altitude [km]")
plt.show()
