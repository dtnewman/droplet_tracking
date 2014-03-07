This project involved two major elements: Detecting water droplets in images and tracking those droplets from one frame to the next. The code for water droplet detection was written by my partner for this project in Matlab and is not available here. I wrote the code for tracking droplets between frames in Python (2.7). 

I encourage you to read over the report (see report_and_project_description.pdf) to find out more about this project.

Please note that to run the movement tracking program, you will need to download and extract a file of images from Dropbox as described below.

Below are brief descriptions of all the program files that I created as well as specifications, where applicable, for packages needed to run these files:


Hungarian.py
Description: Contains the function "hungarian()" which is our implementation of the Hungarian algorithm.
Dependencies: Numpy

Simplex.py
Description: Contains the function "simplex()" which is our implementation of the simplex method.
Dependencies: Numpy

ILP.py
Description: Contains the implementation of the simplex algorithm that uses the Pulp package with the GLPK solver. Note that since we just use this for 
benchmarking purposes, the function "run_ILP()" does not actually return assignments.
Dependencies: Numpy, Pulp. For instructions for installing Pulp package, see: http://pythonhosted.org/PuLP/main/installing_pulp_at_home.html

Hungarian_Munkres_Package.py
Description: Contains the implementation of the Hungarian method that uses the Munkres package.
Dependencies: Numpy, Munkres (see http://software.clapper.org/munkres/)

Figure3.py
Description: Used to generate figure 3 in our writeup
Dependencies: Numpy, matplotlib, Munkres

Figure8.py
Description: Used to generate figure 8 in our writeup
Dependencies: Numpy, matplotlib, Munkres

Figure9.py
Description: Used to generate figure 9 in our writeup
Dependencies: Numpy, matplotlib, Pulp

Figure10.py
Description: Used to generate figure 10 in our writeup
Dependencies: Numpy, matplotlib, Pulp

FigureS5.py
Description: Used to generate figure S5 in our writeup
Dependencies: Numpy, matplotlib

track_droplets.py:
Description: This is the program that actually implements the optimization method (as described in the paper, it utilizes our implementation of the simplex method) to track droplets from frame to frame.
Dependencies: Scipy, Numpy, matplotlib
Notes: The files Simplex.py and frames700to3298.mat must be in the same directory when running this. Additionally, the folder containing this file must have a subfolder named 'images' containing the image files that this script depends on.

These images are not on Github,  since they take up quite a bit of space. Instead, I put these images into a dropbox folder so that they 
could be downloaded separately. The folder is located at the following address: https://www.dropbox.com/s/g6c4rd61kz8ra02/images.zip

If you wish to run this script, please download the zipped file at the above location and unzip the images into a folder named 'images' that should be in the same parent directory as this script. If you have any issues downloading the files please email me at danielnewman@umich.edu.
