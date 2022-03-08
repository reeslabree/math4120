import cvxpy as cp
import numpy as np

def f1(x, A, b):
    k = np.subtract(np.multiply(A, x), b)
    return(np.norm(k, 2))

def h1():
    # declare constants
    A = np.array([
        [1, 2],
        [3, 4],
        [5, 6]
    ], dtype=int)
    
    b = np.array([
        [7],
        [8],
        [9]
    ], dtype=int)
    
    # construct the problem
    x = cp.Variable()
    constraints = []
    obj = cp.Minimize(f1(x, A, b))
    
    # solve
    prob = cp.Problem(obj, constraints)
    prob.solve()
    
    # report
    print("status:", prob.status)
    print("optimal value:", prob.value)
    print("optimal var:", x.value)
    
    
# def h2():
    

# def h3():
    

def main():
    h1()
    # h2()
    # h3()

if __name__ == "__main__":
    main()