The principal objective of these three Python 3.11 scripts is run iteratively 
the Discrete Persistent Structures Extractor (DisPerSE; Sousbie et al. 2011) 
in a set of .dat files. The input files must be in the format of the following example:

# px py
59.55832 -52.32817
63.14221 -54.19222
49.78373 -53.96214
48.62412 -58.09662
65.44768 -53.39888
#


The first step is run the run_delaunay2D.py code. The output must be a .NDnet file, that
is used as an input in the run_MSE.py script. The output of MSE must be (among others)
a .NDskl file. The final step is run the run_skelconv.py file using the .NDskl file as input,
obtaining the .segs file that corresponds to the skeleton of the data.

For more information see the DisPerSE manual at: https://www2.iap.fr/users/sousbie/web/html/index4f3e.html?category/Manual
