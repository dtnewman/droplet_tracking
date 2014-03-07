<h3>Water Droplet Tracker</h3> 

<div style="margin: 0 auto; text-align: center; overflow: hidden;">
  <div style="float: left;">
    <img src="https://github.com/dtnewman/droplet_tracking/blob/master/Progress_first_150_frames.jpeg?raw=true" alt="progress" height="350" width="600">
    <br><i>The yellow lines in the figure above were created by track_droplets.py which tracks the movements of the larger droplets as the move around. In the figure above you can see the program's progress after 150 frames.</i>
  </div>
</div>
====
This project involved two major elements: Detecting water droplets in images and tracking those droplets from one frame to the next. The code for water droplet detection was written by my partner for this project in Matlab and is not available here. I wrote the code for tracking droplets between frames in Python (2.7). While this code was written specifically for tracking the movements of circles for a specific research purpose, the principles can be generalized to other instances where multiple objects need to be tracked in a video or series of images.

I encourage you to read over the report (see report_and_project_description.pdf) to find out more about this project. Please note that to run the movement tracking program, you will need to download and extract a file of images from Dropbox as described below.

Below are brief descriptions of all the program files that I created as well as specifications, where applicable, for packages needed to run these files:


<b>Hungarian.py</b> 
<br><i>Description:</i> Contains the function "hungarian()" which is our implementation of the Hungarian algorithm.
<br><i>Dependencies:</i> Numpy

<b>Simplex.py</b> 
<br><i>Description:</i> Contains the function "simplex()" which is our implementation of the simplex method.
<br><i>Dependencies:</i> Numpy

<b>ILP.py</b> 
<br><i>Description:</i> Contains the implementation of the simplex algorithm that uses the Pulp package with the GLPK solver. Note that since we just use this for 
benchmarking purposes, the function "run_ILP()" does not actually return assignments.
<br><i>Dependencies:</i> Numpy, Pulp. For instructions for installing Pulp package, see: http://pythonhosted.org/PuLP/main/installing_pulp_at_home.html

<b>Hungarian_Munkres_Package.py</b> 
<br><i>Description:</i> Contains the implementation of the Hungarian method that uses the Munkres package.
<br><i>Dependencies:</i> Numpy, Munkres (see http://software.clapper.org/munkres/)

<b>Figure3.py</b> 
<br><i>Description:</i> Used to generate figure 3 in our writeup
<br><i>Dependencies:</i> Numpy, matplotlib, Munkres

<b>Figure8.py</b> 
<br><i>Description:</i> Used to generate figure 8 in our writeup
<br><i>Dependencies:</i> Numpy, matplotlib, Munkres

<b>Figure9.py</b> 
<br><i>Description:</i> Used to generate figure 9 in our writeup
<br><i>Dependencies:</i> Numpy, matplotlib, Pulp

<b>Figure10.py</b> 
<br><i>Description:</i> Used to generate figure 10 in our writeup
<br><i>Dependencies:</i> Numpy, matplotlib, Pulp

<b>FigureS5.py</b> 
<br><i>Description:</i> Used to generate figure S5 in our writeup
<br><i>Dependencies:</i> Numpy, matplotlib

<b>track_droplets.py</b> 
<br><i>Description:</i> This is the program that actually implements the optimization method (as described in the paper, it utilizes our implementation of the simplex method) to track droplets from frame to frame.
<br><i>Dependencies</i>: Scipy, Numpy, matplotlib
<br><i>Notes:</i> The files Simplex.py and frames700to3298.mat must be in the same directory when running this. Additionally, the folder containing this file must have a subfolder named 'images' containing the image files that this script depends on.

These images are not on Github,  since they take up quite a bit of space. Instead, I put these images into a dropbox folder so that they 
could be downloaded separately. The folder is located at the following address: https://www.dropbox.com/s/g6c4rd61kz8ra02/images.zip

If you wish to run this script, please download the zipped file at the above location and unzip the images into a folder named 'images' that should be in the same parent directory as this script. If you have any issues downloading the files please email me at danielnewman  {AT SYMBOL HERE} umich {STANDARD SUFFIX FOR UNIVERSITY HERE}.
