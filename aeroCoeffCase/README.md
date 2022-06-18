# aeroCoeffCase 

This directory stores all the input parameters/code for the computation of the **aerodynamic coefficients** of the **Orion** capsule 
entry in **Mars** atmosphere. 

Main input file ```in.capsule```: sets up the different simulation to be done for different **Ma**, **Kn** & **AOA**. 

```in.capsule``` calls at each iteration another input file ```in.case``` which describes the domain setup, force computation and convergence constraint of the simulation. 
