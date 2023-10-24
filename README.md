The principal objective of these Python scripts is run iteratively the Discrete Persistent Structures Extractor (DisPerSE; Sousbie et al. 2011) in a set of .dat files. 
The format of the input files (first step) must be in two columns px py. The procedure is shown below:

1) The first step is run the run_delaunay2D.py code. The output must be a .NDnet file, that
is used as an input in the run_MSE.py script. 

2) After running MSE, the output must be (among others) a .NDskl file. 

3) The final step is run the run_skelconv.py code using the .NDskl file as input,
obtaining the .segs file that corresponds to the skeleton of the data.

For more information see the DisPerSE manual at: https://www2.iap.fr/users/sousbie/web/html/index4f3e.html?category/Manual
