import cvxpy as cp
import numpy as np

def h1():
    # declare constants
    A = np.array([[1, 2],
                  [3, 4],
                  [5, 6]]) #dtype=int)

    b = np.array([[7],
                  [8],
                  [9]]) #, dtype=int)
    
    # construct the problem
    x = cp.Variable((2,1))
    
    constraints = []
    
    obj = cp.Minimize(cp.norm(A@x-b))
    
    # solve
    prob = cp.Problem(obj, constraints)
    prob.solve()
    
    # report
    print("status:", prob.status)
    print("optimal value:", prob.value)
    print("optimal var:\n", x.value)
    
    
def h2():
    # construct the problem
    x_1 = cp.Variable()
    x_2 = cp.Variable()
    
    constraints = [
            cp.abs(x_1) + cp.abs(x_2) + (x_1**2/x_2) <= 5,
            x_2**(-1) + x_1**4 <= 10,
            x_1 >= 0,
            x_2 >= 1
            ]
    
    obj = cp.Minimize(cp.sqrt(x_1**2+x_2**2+1))

    # solve
    prob = cp.Problem(obj, constraints)
    try:
        prob.solve()
        print("status:", prob.status)
        print("optimal value:", prob.value)
        print("optimal var:\n", x_1.value, x_2.value)
    except:
        print("Problem is not Convex")
   

def h3():
    # construct the problem
    x_1 = cp.Variable(1) 
    x_2 = cp.Variable(1)
    x_3 = cp.Variable(1)

    constraints = [cp.sqrt(2*(x_1**2) + x_1*x_2 + 4*(x_2**2)+4) + ((x_1-x_2+x_3+1)**2/(x_1+x_2)) <= 6,
                   x_1 >= 1,
                   x_2 >= 1,
                   x_3 >= 1]
    
    obj = cp.Minimize(x_1**2 + 2*x_1*x_2 + 2*(x_2**2) + x_3**2 + 3*x_1 - 4*x_2)

    # solve
    prob = cp.Problem(obj, constraints)
    prob.solve()

    # report
    print("status:", prob.status)
    print("optimal value:", prob.value)
    print("optimal vars:\n[", x_1.value, ", ", x_2.value, ", ", x_3.value, "]")
    

def main():
    #print("Problem 1")
    # h1()
    #print("\nProblem 2")
    # h2()
    #print("\nProblem 3")
    h3()

if __name__ == "__main__":
    main()
