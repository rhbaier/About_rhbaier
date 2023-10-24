# -*- coding: utf-8 -*-
"""
Created on 23/10/2023

@author: rbaier@usm.cl
"""
import os

btype='smooth' #boundary conditions
Om='0.315'     #Cosmological parameters
Ol=' 0.685'    #(important to write in this format)
Ok=' 0.00'
h=' 0.673'
w=' -1.00'
cosmo=Om+Ol+Ok+h+w

#location of the .dat files where disperse will run
fileloc = '../disperse_tool_output/'
#just files in correct format
file_extension = '.dat'
files_in_directory = [f for f in os.listdir(fileloc) if f.endswith(file_extension) if f!='test_smooth.dat']


parameters= [' -btype '+btype+ ' -cosmo '+cosmo]


N = len(files_in_directory) #number of files in the directory to run disperse
for i in range(N):
    file = files_in_directory[i]
    parameter = parameters[0]
    # Comando a ejecutar en la terminal
    comand='delaunay_2D '+fileloc+str(file) + str(parameter)  
    os.system(comand)
    
