import numpy as np
from scipy.integrate import quad
import sympy as sp
import sys

# Read command line arguments
expression = sys.argv[1]
a = float(sys.argv[2])
b = float(sys.argv[3])

# Define the symbolic variable
x = sp.Symbol('x')

# Define the integrand as a sympy expression
integrand = sp.sympify(expression)

# Convert the sympy expression to a callable function
f = sp.lambdify(x, integrand, 'numpy')

# Perform numerical integration with complex data type
result, error = quad(f, a, b, complex_func=True)

print("Result:", result)
print("Estimated error:", error)
