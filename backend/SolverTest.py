import numpy as np
import cvxpy as cp

# sample mapping of index to "Course". 
courses = {0:"X1", 1:"X2", 2:"X4", 3:"Y2", 4:"Y3", 5:"Z5"}
# Course prereq DDG
coursePreReqGraph = np.array([[0,0,0,0,0,0], [0,0,0,0,0,0], [1,1,0,0,0,0], [0,0,0,0,0,0], [0,1,0,1,0,0], [0,0,1,0,1,0]])
# What courses are available after completing the courses in this sem
nextAvailCoursesMat = np.array([[0,0,2,0,0,0], [0,0,2,0,2,0], [0,0,0,0,0,2], [0,0,0,0,2,0], [0,0,0,0,0,2], [0,0,0,0,0,0]])
print(coursePreReqGraph)
print(nextAvailCoursesMat)
print(nextAvailCoursesMat + coursePreReqGraph.T)

# What courses are conflicting in terms of time
timeConflictGraph = np.array([[0,0,0,1,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0], [1,0,0,0,0,0], [0,0,0,0,0,0], [0,0,0,0,0,0]])

# What courses do we want to take. Binary vector.
coursesToTake = np.array([1,1,1,1,1,1])
cprg = coursePreReqGraph
nacm = nextAvailCoursesMat
ctt = coursesToTake

#print( nacm, ctt, timeConflictGraph)

# Vector of results
partialSchedules = []

# while np.sum(ctt) != 0:
# Create a binary vector of the schedule to find through optimization
currSched = cp.Variable(6, boolean=True)
#coursesLeft = cp.Variable(ctt)
#nextSem = cp.Variable(nacm)
#tcg = cp.Variable(timeConflictGraph)
tmp = np.array([[1,0,0,0,0,0], [0,1,0,0,0,0], [0,0,0,0,0,0], [0,0,0,1,0,0],[0,0,0,0,0,0],[0,0,0,0,0,0]])
constraints = []
constraints += [timeConflictGraph @ currSched == 0]
constraints += [cp.sum(currSched) <= 2]
#constraints += [1 <= cp.sum(nacm @ currSched)]

objective = cp.Maximize( cp.sum( currSched - ctt ) + cp.sum(nacm @ currSched) )

problem = cp.Problem( objective, constraints )
problem.solve(solver=cp.GLPK_MI)
curSched = currSched.value

print( curSched )

