from pylab import plot, show
from numpy import arange
from sympy import integrate, Symbol

def theta(x):
    if x < 0:
        return 0
    else:
        return 1

def rho(params, r):
    R = params["R"]
    Delta = params["Delta"]
    rho0 = params["rho0"]
    R1 = R - Delta / 2
    R2 = R + Delta / 2
    return rho0 * (theta(R2-r) + theta(r-R1) - 1)

def integrated_charge(params):
    R = params["R"]
    Delta = params["Delta"]
    rho0 = params["rho0"]
    r = Symbol("r")
    s = rho0 * integrate(r**2, (r, R-Delta, R+Delta))
    return s

def get_params():
    nm = 18.8972613 # atomic units
    params = {
            "R": 0.354 * nm,
            "Delta": 0.153 * nm,
            "rho0": 0.87307823919825556,
            }
    return params


r = arange(0, 20, 0.1)
y = [rho(get_params(), x) for x in r]
print integrated_charge(get_params())
plot(r, y)
show()
