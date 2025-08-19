# -*- coding: utf-8 -*-
"""
# Exploring a Quadratic Function

In this notebook, we'll look at the quadratic function:

\[
f(x) = ax^2 + bx + c
\]

We'll compute its values, plot it, and find its roots.
"""

import numpy as np
import matplotlib.pyplot as plt

def quadratic(x, a=1, b=0, c=0):
    """Compute quadratic function f(x) = ax^2 + bx + c."""
    return a*x**2 + b*x + c

# Example: f(x) = x^2 - 2x - 3
a, b, c = 1, -2, -3

"""
## Step 1: Visualizing the function

Let's plot \( f(x) = x^2 - 2x - 3 \) over the range \([-5, 5]\).

"""

x = np.linspace(-5, 5, 400)
y = quadratic(x, a, b, c)

plt.plot(x, y, label=f"${a}x^2 + {b}x + {c}$")
plt.axhline(0, color="black", linewidth=0.8)
plt.axvline(0, color="black", linewidth=0.8)
plt.title("Quadratic Function")
plt.xlabel("x")
plt.ylabel("f(x)")
plt.legend()
plt.grid(True)
plt.show()

"""
## Step 2: Finding the roots

The roots of the quadratic equation are given by the **quadratic formula**:

\[
x = \frac{-b \pm \sqrt{b^2 - 4ac}}{2a}
\]

"""

discriminant = b**2 - 4*a*c
root1 = (-b + np.sqrt(discriminant)) / (2*a)
root2 = (-b - np.sqrt(discriminant)) / (2*a)

print(f"The roots are: x1 = {root1:.2f}, x2 = {root2:.2f}")