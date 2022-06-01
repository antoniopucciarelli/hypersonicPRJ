import numpy as np
import matplotlib.pyplot as plt

#step cpu np nattempt ncoll nscoll c_fxTOT
out0 = np.loadtxt("ref/output_in_time_wp_13.dat", skiprows = 0)
out1 = np.loadtxt("ref/output_in_time_wp_12.dat", skiprows = 0)
out2 = np.loadtxt("ref/output_in_time_wp_11.dat", skiprows = 0)

step0 = out0[:, 0]
npar0 = out0[:, 2]
nsur0 = out0[:, 5]
fx0   = out0[:, 6]

step1 = out1[:, 0]
npar1 = out1[:, 2]
nsur1 = out1[:, 5]
fx1   = out1[:, 6]

step2 = out2[:, 0]
npar2 = out2[:, 2]
nsur2 = out2[:, 5]
fx2   = out2[:, 6]

plt.figure(1)
plt.plot(step0, npar0)
plt.plot(step1, npar1)
plt.plot(step2, npar2)
plt.title("Number of particles per time step")

plt.figure(2)
plt.plot(step0, nsur0)
plt.plot(step1, nsur1)
plt.plot(step2, nsur2)
plt.title("Number of gas-surface collisions per time step")

plt.figure(3)
plt.plot(step0, fx0)
plt.plot(step1, fx1)
plt.plot(step2, fx2)
plt.title("Drag")

drag = np.ones((len(step1), 1))*0.0043

plt.figure(3)
plt.plot(step1, drag, "--")
plt.title("Drag")

plt.show()
