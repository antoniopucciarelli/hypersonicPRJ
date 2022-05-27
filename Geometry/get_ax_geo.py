import numpy as np
import matplotlib.pyplot as plt

data = np.loadtxt('axis_orion.dat',
                     skiprows = 1,
                     delimiter=',')
#sort dataset
i = np.argsort(data[:,0])
data = data[i,:]
#problems in the first and last part -> sort for increasing and decreasing y
#first part
data_1 = data[0:24,:]
j = np.argsort(data_1[:,1])
data_1 = data_1[j,:]
data[0:24,:] = data_1
#last part
data_2 = data[84:,:]
k = np.argsort(data_2[:,1])
data_2 = data_2[k,:]
data[84:,:] = np.flip(data_2, axis=0)
#extract x and y coordinate
xx = data[:,0]
yy = data[:,1]
#put the shield in the origin and mirror x coordinate
xx = xx - max(xx)
xx = -xx
#add specular component
xx_add = np.flip(xx[1:-1])
yy_add = - np.flip(yy[1:-1])

xx = np.concatenate([xx, xx_add])
yy = np.concatenate([yy, yy_add])

#change rotation law
xx = np.flip(xx)
yy = np.flip(yy)

plt.figure(1)
plt.plot(xx,yy)
plt.title("2D Orion GEO")
plt.show()

##write geometry to SPARTA data file

f = open("data.simple_orion_ax", "w")

f.write("2D geometry from orion_simple\n")
f.write("\n")
f.write(str(len(xx))+" points\n")
f.write(str(len(xx))+" lines\n")
f.write("\n")

#write points
f.write("Points\n")
f.write("\n")

for ii in range(len(xx)):
	f.write(str(ii+1)+ " " + str(xx[ii]) + " " + str(yy[ii]) + "\n")

#write lines
f.write("\n")
f.write("Lines\n")
f.write("\n")

for ii in range(len(xx)-1):
	f.write(str(ii+1) + " " + str(ii+1) + " " + str(ii+2) + "\n")
#add last line
f.write(str(len(xx)) + " " + str(len(xx)) + " " + str(1) + "\n")

f.close()

