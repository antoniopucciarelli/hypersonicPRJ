#!/bin/sh

rm -r grid_output *.pvd

#my_pvpython=/home/raffaele/ParaView-5.10.0-MPI-Linux-Python3.9-x86_64/bin/pvpython


#$my_pvpython grid2paraview.py grid_descriptor.txt grid_output -r ../fField/flow_field.*

my_pvpython grid2paraview.py grid_descriptor.txt grid_output -r ../fField.flow_field.*

#paraview *.pvd 


