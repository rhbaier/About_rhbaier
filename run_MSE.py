# -*- coding: utf-8 -*-
"""
Created on 23/10/2023

@author: rbaier@usm.cl
"""

import os


sigma='3.0' #persistence thereshold

fileloc = '../NDnet_directory/' #directory with NDnet files
file_extension = '.NDnet'
files_in_directory = [f for f in os.listdir(fileloc) if f.endswith(file_extension) ]

parameters= [' -upSkl ' +' -nsig '+sigma]
N = len(files_in_directory)
for i in range(N):
    archivo = files_in_directory[i]
    parameter = parameters[0]
    # Comando a ejecutar en la terminal
    comand='mse '+fileloc+str(archivo) + str(parameter)  
    os.system(comand)
