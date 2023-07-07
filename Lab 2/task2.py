import numpy as np
import numpy.linalg as la

a = np.arange(1, 10).reshape(3, 3)
b = np.array([[3, 1, 4], [2, 6, 1], [2, 9, 7]])

# A + B
c = a + b
print(c)
print()

# A X B
d = np.dot(a, b)
print(d)
print()

# Determinate of A
det_a = la.det(a)
print(det_a)
print()

# Inverse of B 
inv_b = la.inv(b)
print(inv_b)
print()

# Eigenvalues of A
eigvals_a = la.eigvals(a)
print(eigvals_a)
print()
