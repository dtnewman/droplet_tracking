# This file contains the function to solve our distance minimization
# problem using the Pulp package for python. By default, this package
# uses the glpk solver, which is implemented in c.
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
# and finds assignments of points from one frame to the next that 
# minimize the overall distance.
#


import numpy as np
import random
import time
from pulp import *


def run_ILP(matrix):
    
    start = time.time()

    m, n = np.shape(matrix)

    Rows = range(m)
    Cols = range(n)

    prob = LpProblem("MinimizeSumDistances", LpMinimize)

    # setup binary decision variables
    assign_vars = LpVariable.dicts("Assignment",(Rows,Cols),0,1,LpInteger)

    # add objective function that minimizes distances                        
    prob += lpSum(assign_vars[i][j]*(matrix[i][j]) for i in range(m) 
                                                        for j in range(n))

    # add constraint that each point in the first frame must be matched up 
    # with exactly one point in the second frame
    for i in Rows:
        prob += lpSum(assign_vars[i][j] for j in Cols) == 1

    # add constraint that each point in the second frame must be matched up 
    # with exactly one point in the first frame
    for j in Cols:
        prob += lpSum(assign_vars[i][j] for i in Rows) == 1


    solutionFound = prob.solve()
    obj_func_value = value(prob.objective)
    total_time = time.time()-start

    return obj_func_value, total_time 


if __name__ == '__main__':
 
    test_matrix = np.array([[5,9,3,6],[8,7,8,2],[6,10,12,7],[3,10,8,6]])
    obj_func_value, total_time = run_ILP(test_matrix)
    print obj_func_value, total_time
    



    

