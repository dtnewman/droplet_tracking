# This file contains our implementation of the simplex method. Please
# note that the "simplex" function setup below is designed specifically 
# for our problem and is not a general purpose solver. 
#
# In our problem, we are matching up points from one frame in an image
# to the next. The simplex algorithm implemented below is setup to solve 
# a linear program with the following general form:
#
# MINIMIZE Z = C*X, where C is a square cost matrix and X is a square
#                   matrix
# Subject to:   Sum(Xij) in row i = 1 for all rows
#               Sum(Xij) in column i = 1 for all columns
#               Xij >= 0
#
# The function below takes in a square cost matrix (containing distances
# from all points in the first frame to all points in the second frame)
# and returns assignments of points from one frame to the next that 
# minimize the overall distance.

import numpy as np
import time

def simplex(cost_matrix):
    M =100000 #set M to arbitrarily high value 

    start = time.time()
    n = np.shape(cost_matrix)[0]
    simplex_matrix = np.zeros((n*2,n*n))

    
    #setup constraints in simplex matrix
    for i in range(n):
        for j in range(n):
            simplex_matrix[i][j+i*n] = 1
    
    for i in range(n,2*n):
        for j in range(n):
            simplex_matrix[i][i-n+j*n] = 1

   
    #Add artificial variables by appending identity matrix
    simplex_matrix = np.hstack((simplex_matrix,np.identity(2*n)))

    
    #add constraints
    column_to_add = np.zeros(2*n).reshape(2*n,1)
    simplex_matrix = np.hstack((simplex_matrix,column_to_add))
    height, width = np.shape(simplex_matrix)
    for i in range(n*2):
        simplex_matrix[i][width-1] = 1
    
    #add objective row using values from cost matrix
    simplex_matrix = np.vstack((simplex_matrix,np.zeros(width))) 
    for i in range(n*n):
        simplex_matrix[height][i] = 2*M-cost_matrix.flatten()[i]
    height+=1

    #~ print simplex_matrix.astype(int)
    
    #keep looping until all values in the last row are 0 or negative
    while np.max(simplex_matrix[height-1][0:width-1]) > 0:
        #find the max value in the last row and the column that it is in
        max_value =  np.max(simplex_matrix[height-1][0:width-1])
        
        #get pivot column
        list_of_columns = np.where(simplex_matrix[height-1] == max_value)[0]
        col = list_of_columns[np.random.randint(len(list_of_columns))]
        min_ratio = np.inf
        min_ratio_row = -1
        
        # get the ratio for each number in that column compared to the last
        # column in order to find the pivot row        
        for i in range(height-1):
            if simplex_matrix[i][col] <> 0:
                ratio = simplex_matrix[i][width-1]/simplex_matrix[i][col]
                if 0 < ratio < min_ratio:
                    min_ratio = ratio
                    row = i        
                elif ratio == 0 and simplex_matrix[i][col] > 0:
                    min_ratio = ratio
                    row = i
        
        assert min_ratio <> -1 # For debugging purposes... makes sure valid
                               # ratio was found        

        # get the pivot_value
        pivot_value = simplex_matrix[row][col]
                
        # divide row containing pivot so that the pivot value is equal to 1
        simplex_matrix[row] = simplex_matrix[row]/pivot_value
        
        # subtract multiple of pivot row from each column such that the
        # pivot column only contains 0's outside of the pivot value
        for i in range(height):
            if i <> row:
                multiple = simplex_matrix[i][col]/pivot_value
                simplex_matrix[i] -= multiple * simplex_matrix[row]
    
    #extract assignments
    assignments = np.zeros(n*n)
    
    for i in range(n*n):
        if np.sum(np.absolute(simplex_matrix[:,i])) == 1 and np.max(np.absolute(simplex_matrix[:,i]))== 1:
            assignments[i] = np.sum(simplex_matrix[:,i]*simplex_matrix[:,width-1])
    
    assignments = np.reshape(assignments,(n,n))
    
    obj_func_value = np.sum(assignments * cost_matrix)
    total_time = time.time()-start
    assert np.sum(assignments) == n
    return obj_func_value, total_time, assignments.astype(int)

    
    

if __name__ == '__main__':
    #~ test_matrix = np.array([[1,4],[3,5]])
    #~ test_matrix = np.array([[1,3,3],[3,2,3],[3,3,2]])
    #~ test_matrix = np.array([[127,668,455],[550,156,327],[349,887,804]])
    test_matrix = np.array([[5,9,3,6],[8,7,8,2],[6,10,12,7],[3,10,8,6]])
    obj_func_value, time, assignments = simplex(test_matrix)
    print obj_func_value, time
    print assignments
    
