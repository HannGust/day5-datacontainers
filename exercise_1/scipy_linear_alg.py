"""
The code for the exercise 1 on day 5.
"""

import numpy as np
import scipy.linalg
 
# 1a.
print("1.a) Solving a linear system of equations.")
print()

A = [[1, 2, 3],
     [4, 5, 6],
     [7, 8, 9]]

print("Matrix A:", A)

# 1b.
b = [1, 2, 3]
print("Vector b:", b)

# 1c.
try:
    x = scipy.linalg.solve(A, b)
    print("Solution x to Ax = b:", x)
    print(type(x))

except:
    print("Error occured when trying to solve the equation A*x = b.")
    print("Is the matrix A singular perhaps?: ")
    print("det A =", scipy.linalg.det(A))
    x = None

# 1d.
if x:
   print("Checking that the solution is correct:")
   print("A*x = ", A*x)
   print("b =", b)


# 1e.
print()
print("1.e) Solving a linear matrix equation.")
print()

B = np.random.random((3,3))

print("Matrix A:", A)

print("Matrix B:", B)

try: 
    X = scipy.linalg.solve(A, B)
except:
    print("Error occured when trying to solve the equation A*X = B.")
    print("Is the matrix A singular perhaps?: ")
    print("det A =", scipy.linalg.det(A))
    X = None

if X:
    print("Checking that X is a correct solution:")
    print("A*X =", A*X)
    print("B =", B)

