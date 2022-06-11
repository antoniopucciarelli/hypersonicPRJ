#plot reference quantities for martian re-entry
import numpy as np
import matplotlib.pyplot as plt

data_rho = np.loadtxt('martian_rho.dat',
                     delimiter=',')
#altitude
data_h   = np.loadtxt('altitude_time.dat',
                     delimiter=';')
#valocity
data_v  = np.loadtxt('velocity_time.dat',
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

#altitude
plt.figure(2)
plt.plot(data_h[:,0],data_h[:,1])
plt.title("Altitude time")
plt.xlabel("Time [s]")
plt.ylabel("Altitude [km]")
plt.show()

#velocity
plt.figure(3)
plt.plot(data_v[:,0],data_v[:,1])
plt.title("Velocity time")
plt.xlabel("Time [s]")
plt.ylabel("Velocity [km/s]")
plt.show()

#Temperature
plt.figure(4)
plt.plot(data_T[:,0],data_T[:,1])
plt.title("Temperature altitude")
plt.xlabel("Temperature [K]")
plt.ylabel("Altitude [km]")
plt.show()

