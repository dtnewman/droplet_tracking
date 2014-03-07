# This is the script that actually incorporates optimization to match
# up droplets between frames. Note that this script uses the images in 
# the folder 'images', which were NOT included with our submission, 
# since they take up quite a bit of space. Instead, we put these images
# into a dropbox folder so that they could be downloaded separately.
# The folder is located at the following address:
# https://www.dropbox.com/s/31fecs15dsthkg8/images.zip
#
# We will make sure that the relevant files are kept there at least 
# until this project is graded. If you wish to run this script, please
# download the zipped file at the above location and unzip the images
# into a folder named 'images' that should be in the same parent 
# directory as this script. If you have any issues downloading the files
# please email us at dnewman@fas.harvard.edu and daniel@fas.harvard.edu

import numpy as np
import scipy.io
import matplotlib.pyplot as plt
import matplotlib.cbook as cbook
import time
from Simplex import *

START_FRAME = 0
IMAGE_WIDTH = 960
IMAGE_HEIGHT = 540
MIN_RADIUS = 9.0 # disregard circles with radii under this
MAX_DISTANCE = 50 # set this as the maximum distance we presume a circle
                  # can move between two frames


plt.ion() #puts plots into interactive mode
fig, axs = plt.subplots()
 
# load data from .mat file containing outputs from Hough Transforms 
data = scipy.io.loadmat('frames700to3298.mat')


total_num_images = len(data['droplet_radius'][0])
print "Total number of images:", total_num_images  


# loop through each data set in frames700to3298.mat and run simplex 
# method to minimize distances from points in one frame to the next
for image_num in range(START_FRAME,total_num_images-1):

    print "image num", image_num
    
    #extract data from .mat file
    x_list1 = data['X'][0][image_num]
    y_list1 = data['Y'][0][image_num]
    x_list2 = data['X'][0][image_num+1]
    y_list2 = data['Y'][0][image_num+1]
    radii1 = data['droplet_radius'][0][image_num]
    radii2 = data['droplet_radius'][0][image_num+1]

    
    # combine all the data into two sets
    set1 = np.array([-10,-10])
    set2 = np.array([-10,-10])
    set1_size = 1
    set2_size = 1
    for i in range(len(x_list1)):
        if radii1[i][0] > MIN_RADIUS:
            set1_size += 1
            set1 = np.vstack((set1,np.array([x_list1[i][0],IMAGE_HEIGHT-y_list1[i][0]]))) #flip image along x-axis
    for i in range(len(x_list2)):
        if radii2[i][0] > MIN_RADIUS:
            set2_size += 1
            set2 = np.vstack((set2,np.array([x_list2[i][0],IMAGE_HEIGHT-y_list2[i][0]]))) #flip image along x-axis

    #add dummy points if one set is larger than the other
    while set1_size > set2_size:
        set2 = np.vstack((set2,np.array([10000,10000])))
        set2_size += 1
    while set2_size > set1_size:
        set1 = np.vstack((set1,np.array([10000,10000])))
        set1_size += 1

    # put the corresponding image in the background of the plot
    # See notes at beginning of file regarding image folder.
    im = plt.imread("images/image"+str(image_num+1)+".tif")
    implot = axs.imshow(im)
    plt.title("Frame " + str(image_num))
    
    print "Set sizes:",set1_size
    
    # check if the data set has any points in it (disregarding the first
    # point to make the code above cleaner)
    if set1_size > 1: 
        #create distance matrix
        distance_matrix = []

        for i in range(set1_size):
            distance_matrix.append([])
            for j in range(set2_size):
                distance = np.linalg.norm(set1[i]-set2[j])
                if distance < MAX_DISTANCE:
                    distance_matrix[i].append(distance)
                else:
                    distance_matrix[i].append(99999)
        
        distance_matrix = np.array(distance_matrix)

        # run simplex algorithm on matrix to get assignments that minimize the
        # total distance
        obj_func_value, time, assignments = simplex(distance_matrix)
        
        print "Time for Simplex method to solve", time



        # extract values from assignments matrix and plot the lines
        # that match up points in first set to second set
        for i, row in enumerate(assignments):
            index=np.where(row==1)[0][0]
            if distance_matrix[i][index] < MAX_DISTANCE:
                plt.plot([set1[i][0],set2[index][0]],[set1[i][1],set2[index][1]], c='y')
        
    if image_num % 1 == 0:
        plt.savefig('Frame_' + str(image_num) + '.png')
    plt.xlim(0,IMAGE_WIDTH)
    plt.ylim(0,IMAGE_HEIGHT)    
    plt.pause(0.001)
    if image_num == 1:
        time.sleep(1)
    


