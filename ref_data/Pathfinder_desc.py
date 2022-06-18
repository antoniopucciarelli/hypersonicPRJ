# data taken from 1997 Moss Journal

import numpy as np
import matplotlib.pyplot as plt

# altitude [km]
h = np.array([141.8, 130.9, 119.0, 110.1, 100.0, 95, 90.2, 85.1, 80.0, 75.0,
		65.0, 56.1])
# velocity [m/s]
v = np.array([7463.1, 7463.1, 7468.6, 7472.8, 7477.3, 7479.5, 7481.5, 7483.3,
		7484.6, 7484.6, 7453.9, 7431.3])
# wall temperature [K]
Tw = np.array([300, 389, 470, 560, 675, 750, 824, 900, 950, 1000, 1100, 1500])
# Kninf -> related to Pathfinder Pf
KnPf = np.array([5.5e1, 1.32e1, 2.76, 8.47e-1, 2.22e-1, 1.13e-1, 5.98e-2,
		3.01e-2, 1.15e-2, 7.67e-3, 1.96e-3, 5.60e-4])
# Pathfinder length
LPf = 2.65
# Orion length
LOr = 5.03
# Orion Kn
KnOr = KnPf*LPf/LOr
# asimptotic temperature [K]
Tinf = 137.4

# Ma computation
#molecular masses and mass fraction
mmCO2 = 7.31E-26  #kg -> mass of just one molecule
mmN2  = 4.65E-26  #kg
#mass fraction
YCO2  = 0.97
YN2   = 0.03
#equivalent R computation
kB = 1.380649e-23

RCO2 = kB/mmCO2 # already in SI units
RN2  = kB/mmN2

# equivalent gas constant for the mixture
R = YCO2*RCO2 + YN2*RN2
cvN2  = (3/2+1)*RN2   #sum of contribution of internal and rotational energy le>
cvCO2 = (3/2 + 2)*RCO2 # each rotational 1/2*R -> CO2 is not bi-molecular
                       # so rotational energy level is higher
#mixture cv and cp
cv = YCO2*cvCO2 + YN2*cvN2
cp = YCO2*(RCO2+cvCO2) + YN2*(RN2+cvN2)
#computing gamma for the mixture
gamma = cp/cv

#computing speed of sound
c = np.sqrt(gamma*R*Tinf)
#Mach number computation
Ma = v/c

# print quantity
ll = []
for ii in range(len(KnOr)):
    if KnOr[ii]<10 and KnOr[ii]>0.01:
         ll.append(ii)

#deleting quantity out of affordable computational cost range

h    = h[ll]
KnOr = KnOr[ll]
v    = v[ll]
Tw   = Tw[ll]
Ma   = Ma[ll]

print("*** altitude = " + str(h) + " ***")
print("*** Kn = " + str(KnOr) + " ***")
print("*** velocity = " + str(v) + " ***")
print("*** T wall = " + str(Tw) + " ***")
print("*** T inf = " + str(Tinf) + " ***")

print("*** NUMBER OF SIMULATION TO PERFORM = " + str(len(ll)))

a = input("Do you want to show charts? [y/n]")

if a=="y":
    plt.figure(1)
    plt.semilogx(KnOr, h)
    plt.title("Kn inf Orion")
    plt.xlabel("Kn inf")
    plt.ylabel("Altitude [km]")
    plt.show()

    plt.figure(2)
    plt.plot(Tw, h)
    plt.title("Wall temperature")
    plt.xlabel("Wall temperature [K]")
    plt.ylabel("Altitude [km]")
    plt.show()

    plt.figure(3)
    plt.plot(Ma, h)
    plt.title("Ma inf")
    plt.xlabel("Ma")
    plt.ylabel("Altitude [km]")
    plt.show()


