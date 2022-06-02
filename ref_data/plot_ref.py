#plot reference quantities for martian re-entry
import numpy as np
import matplotlib.pyplot as plt

data_rho = np.loadtxt('martian_rho.dat',
                     delimiter=',')

#plot to check the extracted data
plt.figure(1)
plt.semilogx(data_rho[:,0],data_rho[:,1])
plt.title("Martian density")
plt.xlabel("Density [kg/m3]")
plt.ylabel("Altitude [km]")
plt.show()
