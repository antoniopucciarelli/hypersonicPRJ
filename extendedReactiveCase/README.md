# basicReactiveCase 

This directory stores all the input parameters/code for the computation of the **flow properties** of the **Orion** capsule 
entry in **Mars** atmosphere. 

Main input file ```in.capsule```: sets up the different simulation to be done for **C** & **O** based combustion. 

```in.capsule``` calls at each iteration another input file ```in.case``` which describes the domain setup, flow properties computation and reaction properties for the simulation. 