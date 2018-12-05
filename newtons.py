import math
import sympy as sym

#
# newtons method
#

def newtons(f, x0, tol=0.0001, h=0.001, maxit=100):
    
    # create update equation
    g = sym.lambdify((x),f/f.diff())
    update = lambda xn, h: xn - h*g(xn)

    # start loop
    xn = x0
    for i in range(maxit):
        if abs(xn) <= tol:
            return xn
        xn = update(xn, h)
    
    print("Did not converge")
    return xn

#
# testing
#

# define function
x = sym.symbols("x")
f = x-2**(-x)

# find root approximation using newtons
x_initial = 7/2 - math.sqrt(33)/2
root = newtons(f, x_initial, h=0.00001, tol=0.000001, maxit=10000000)

# display root approximation and error
f_check = sym.lambdify((x), f)
print("root approximation: ", root)
print("error: ", abs(f_check(root)))

