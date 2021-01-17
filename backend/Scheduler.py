import numpy as np
import cvxpy as cp

def entryPoint(coursesCompleted, coursesDesired, startSem):
    """
    This is the entry point function for the ILP scheduler.

    coursesCompleted: a list of courses that the person already has credits for
    coursesDesired: a list of courses that the person wants to take.
    startSem: either 0 or 1 indicating wether this is winter or fall

    Returns: list of lists containing the schedules which will permit the
    student to take the desired courses.

    """
    # First, BFS for a list of all the courses that need to be scheduled. 
    allNecessaryCourses = bfsPreReqListGenerator(coursesDesired)

    # Next, prune out the courses that the student has credit for.
    remainingCourses = pruneCourses(allNecessaryCourses, coursesCompleted)

    # Generate the course frontiers
    fallFrontier = genFallFrontier()
    winterFronter = genWinterFrontier()

    iteration = startSem
    result = []

    while np.sum(remainingCourses) != 0:
        # Generate the variable which will contain the optimization result
        currSched = cp.Variable(graphSize, boolean=True)

        # Set the constraints based on which semester it is (Fall or Winter)
        constraints = []
        if iteration % 2 == 0:
            constraints = constraintsFall(currSched)
        else:
            constraints = constraintsWinter(currSched)

        # Get the set of courses that we can currently take with a weighted 
        # heuristic
        coursesToPickFrom = genCoursesToPickFrom(remainingCourses, iteration, fallFrontier, winterFrontier)

        # Solve the ILP problem
        objective = cp.Maximize( cp.sum(currSched - remainingCourses) + cp.sum(cp.multiply( currSched, coursesToPickFrom )))
        prob = cp.Problem(objective, constraints)
        problem.solve( solver=cp.GLPK_MI )
        sched = currSched.value

        # Generate the results
        result.append(genScheduleNames(sched))

        # Update the frontiers for the next iteration
        fallFrontier, winterFrontier = updateFrontiers(fallFrontier, winterFrontier, iteration)

        # Update iteration counter.
        iteration = iteration + 1

        # Update the remaining courses left to schedule
        remainingCourses = remainingCourses - sched

    return result










