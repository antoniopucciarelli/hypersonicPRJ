#!/bin/sh

rm -r surf_output *.pvd

my_pvpython=/home/raffaele/ParaView-5.10.0-MPI-Linux-Python3.9-x86_64/bin/pvpython

$my_pvpython surf2paraview.py ../geometry/data.orionSimple surf_output -r ../dump/Kn1/Ma1/AOA1//flowField/surf_heat_flux.*

paraview *.pvd 


