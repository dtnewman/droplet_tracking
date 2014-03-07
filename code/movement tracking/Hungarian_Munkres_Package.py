# This file contains the function for running the Hungarian Algorithm
# using the Munkres package which is available for Python. 
#
# In our problem, we are matching up points from one frame in an image
# to the next. The function "hungarian" below takes in a square matrix
# containing distances between points and returns a matrix containing
# assignments of points from the first image to the second
#
# The function below takes in a square cost matrix (containing distances
# from all points in the first frame to all points in the second frame)
# and returns assignments of points from one frame to the next that 
# minimize the overall distance.

from munkres import Munkres, print_matrix
import numpy as np
import random
import time


def munkres_package_Hungarian(matrix):
    orig_matrix = matrix
    m = Munkres()
    start = time.time()
    indexes = m.compute(matrix)
    obj_func_value = 0.0
    for row, column in indexes:
        value = orig_matrix[row][column]
        obj_func_value += value
    total_time = time.time()-start
    return obj_func_value, total_time, indexes


if __name__ == '__main__':
    matrix = np.array([[5,9,3,6],[8,7,8,2],[6,10,12,7],[3,10,8,6]])
    obj_func_value, total_time, indexes = munkres_package_Hungarian(matrix)
    print obj_func_value, total_time
    print indexes

