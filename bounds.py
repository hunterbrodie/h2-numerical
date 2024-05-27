import numpy as np
import random
import math

def x(r, s, c):
    return (r**2-s**2)/4/c

def y(r, s, c):
    return (r**2-(x(r, s, c) + c)**2)**0.5

def r(x, y, c):
    return ((x+c)**2+y**2)**0.5

def s(x, y, c):
    return ((x-c)**2+y**2)**0.5

def bounds(r1, s1, r2, s2, c):
    return (np.linalg.norm([x(r1, s1, c) - x(r2, s2, c), y(r1, s1, c) - y(r2, s2, c)]), np.linalg.norm([x(r1, s1, c) - x(r2, s2, c), y(r1, s1, c) + y(r2, s2, c)]))


print("Enter C")
c = int(input())
print("Enter Radial Cutoff")
r_max = int(input())
print("Enter Radial Grid Size")
r_size = int(input())
#print("Enter Internuclear Grid Size")
#t_size = int(input())

precision = 5

h = np.around(r_max / r_size, precision)

coords = set()

for i in range(r_size):
    r = np.around(i * h, precision)
    mi = np.around(abs(2 * c - r), precision)
    ma = np.around(2 * c + r, precision)
    print(r, end =", ")
    print(mi, end=", ")
    print(ma, end=", ")
    print(np.around((ma - mi) / h, precision))


sorted_coords = sorted(coords, key=lambda element: (element[0], element[1]))
