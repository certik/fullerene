from pylab import plot, show
from numpy import arange

def theta(x):
    if x < 0:
        return 0
    else:
        return 1

rho0 = 1.0
def rho(r):
    R = 0.354
    Delta = 0.153
    R1 = R - Delta / 2
    R2 = R + Delta / 2
    return rho0 * (theta(R2-r) - theta(r-R1))


r = arange(0, 1, 0.01)
y = [rho(x) for x in r]
plot(r, y)
show()
