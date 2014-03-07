# This file contains our implementation of the Hungarian Algorithm. 
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

import numpy as np
import random
import time



def hungarian(matrix):
    start = time.time()
    orig_matrix = matrix.copy()
    n = np.shape(matrix)[0]
    continue_on = True
    
    # subtract the minimum value of each row from all values in that row
    for i in range(n):
        matrix[i] = matrix[i] - np.min(matrix[i])
    
    for j in range(n):
        matrix[:,j] = matrix[:,j]-np.min(matrix[:,j])
    
    
    rows_crossed_out = np.zeros(n)
    cols_crossed_out = np.zeros(n)    
    assignments = np.zeros((n,n),dtype=np.int64)

    while (np.sum(rows_crossed_out)+np.sum(cols_crossed_out) < n and continue_on):
        assignments = np.zeros((n,n),dtype=np.int64)
        old_assignment_sum = np.inf
        matrix_copy = matrix.copy()
        
        # try to make assignments
        while np.sum(assignments) <> old_assignment_sum:
            old_assignment_sum = np.sum(assignments)
            for i in range(n):
                if n-np.count_nonzero(matrix_copy[i]) == 1:
                    zero_position = np.where(matrix_copy[i]==0)[0][0]
                    assignments[i][zero_position] = 1
                    matrix_copy[i] += 1
                    matrix_copy[:,zero_position] += 1

            for j in range(n):
                if n-np.count_nonzero(matrix_copy[:,j]) == 1:
                    zero_position = np.where(matrix_copy[:,j]==0)[0][0]
                    assignments[zero_position][j] = 1
                    matrix_copy[zero_position] += 1
                    matrix_copy[:,j] += 1
        
        
        if old_assignment_sum < n:
            rows_crossed_out = np.zeros(n)
            cols_crossed_out = np.zeros(n)
            
            for i in range(n):
                if sum(assignments[i]) == 0:
                    rows_crossed_out[i] = 1
            
            # keep looping until no changes are being made
            while 1:
                rows_crossed_out_last = rows_crossed_out.copy()
                cols_crossed_out_last = cols_crossed_out.copy()
                for i in range(n):
                    if rows_crossed_out[i] == 1:
                        for j in range(n):
                            if matrix[i][j] == 0:
                                cols_crossed_out[j] = 1
                for j in range(n):
                    if cols_crossed_out[j] == 1:
                        for i in range(n):
                            if assignments[i][j] == 1:
                                rows_crossed_out[i] = 1
                
                if (np.array_equal(rows_crossed_out_last, rows_crossed_out) 
                    and np.array_equal(cols_crossed_out_last,cols_crossed_out)):
                    break #exit while loop if no changes were made
              
            rows_crossed_out = 1-rows_crossed_out
            
            minvalue = np.max(matrix)
            
            # get minimum value not crossed out
            for i in range(n):
                if rows_crossed_out[i] == 0:
                    for j in range(n):
                        if cols_crossed_out[j] == 0:
                            value = matrix[i][j]
                            if value < minvalue:
                                minvalue = value
            
            # add minimum value to all crossed out elements (add twice if 
            # element is crossed out twice)
            for i in range(n):
                for j in range(n):
                    matrix[i][j] += minvalue*(rows_crossed_out[i]+cols_crossed_out[j])

            # subtract the minimum value in the matrix from every value in the matrix
            matrix = matrix - np.min(matrix)
        
        else:
            break
       
    total_time = time.time()-start
    return np.sum(orig_matrix*assignments), total_time, assignments

        
  
if __name__ == '__main__':
    #~ test_matrix = np.array([[10,19,8,15,19],[10,18,7,17,19],[13,16,9,14,19],[12,19,8,18,19],[14,17,10,19,19]])
    test_matrix = np.array([[11,7,10,17,10],[13,21,7,11,13],[13,13,15,13,14],[18,10,13,16,14],[12,8,16,19,10]])
    value_Hungarian, time, assignments = hungarian(test_matrix)
    print value_Hungarian, time
    print assignments

    
