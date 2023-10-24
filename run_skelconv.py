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
smooth='100 ' #persistence thereshold

fileloc = '../running/' #directory with NDskl files
file_extension = '.NDskl'
files_in_directory = [f for f in os.listdir(fileloc) if f.endswith(file_extension) ]

parameters= [' -to segs_ascii -cosmo ' + cosmo]
N = len(files_in_directory)
for i in range(N):
    archivo = files_in_directory[i]
    parameter = parameters[0]
    # Comando a ejecutar en la terminal
    comand='skelconv '+fileloc+str(archivo) + ' -breakdown -smooth '+smooth+str(parameter)  
    os.system(comand)
