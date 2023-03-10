"""
The code for the exercise 1 on day 5.
"""

import numpy as np
import scipy.linalg
 
# 1a.
print("1.a) Solving a linear system of equations.")
print()

A = [[9, 2, 3],
     [4, 7, 6],
     [1, 8, 9]]

print("Matrix A:", A)
print()

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

# 1d.
if x is not None:
   print("Checking that the solution is correct:")
   print("A*x = ", A @ x)
   print("b =", b)


# 1e.
print()
print("1.e) Solving a linear matrix equation.")
print()

B = np.random.random((3,3))

print("Matrix A:", A)
print()
print("Matrix B:", B)
print()

try: 
    X = scipy.linalg.solve(A, B)
except:
    print("Error occured when trying to solve the equation A*X = B.")
    print("Is the matrix A singular perhaps?: ")
    print("det A =", scipy.linalg.det(A))

if X is not None:
    print("Checking that X is a correct solution:")
    print("A*X =", A @ X)
    print()
    print("B =", B)
    print()
    print("Difference A@X-B:" )
    print(A @ X - B)
    print()

# 1f.
eigvalsA, eigvecA  = scipy.linalg.eig(A)

print()
print("Eigenvalues of A:")
print(eigvalsA)
print()
print("Eigenvectors of A: ")
print(*(eigvecA[:,i] for i in range(3)))
print()

# 1g.
detA = scipy.linalg.det(A)

invA = scipy.linalg.inv(A)

print()
print("Determinant of A:", detA)
print()
print("Inverse of A =")
print(invA)
print()

# 1h.
norm_types = ['fro', 'nuc', np.inf, -np.inf, 1, 2]
Anorms = [scipy.linalg.norm(A, ord=ord) for ord in norm_types]

print("Matrix norms of A:")
for i in range(len(Anorms)):
    print(norm_types[i], Anorms[i])
