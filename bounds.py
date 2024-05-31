import numpy as np
import random
import math

precision = 5

def x(r, s, c):
    return np.around((r**2-s**2)/4/c, precision)

def y(r, s, c):
    if r**2 - (x(r, s, c) + c)**2 < 0:
        return 0
    return (r**2-(x(r, s, c) + c)**2)**0.5

def r(x, y, c):
    return ((x+c)**2+y**2)**0.5

def s(x, y, c):
    return ((x-c)**2+y**2)**0.5

def bounds(r1, s1, r2, s2, c):
    return (np.linalg.norm([x(r1, s1, c) - x(r2, s2, c), y(r1, s1, c) - y(r2, s2, c)]), np.linalg.norm([x(r1, s1, c) - x(r2, s2, c), y(r1, s1, c) + y(r2, s2, c)]))


print("Enter C")
c = np.around(float(input()), precision)
print("Enter Radial Cutoff")
r_max = int(input())
print("Enter Radial Grid Size")
r_size = int(input())
#print("Enter Internuclear Grid Size")
#t_size = int(input())


h = np.around(r_max / r_size, precision)

coords = set()

for i in range(r_size):
    r = np.around(i * h, precision)
    mi = np.around(abs(2 * c - r), precision)
    ma = np.around(2 * c + r, precision)
    distance = int((ma - mi) / h)
    for j in range(distance + 1):
        s = np.around(mi + h * j, precision)
        coords.add((r, s))
        coords.add((s, r))


sorted_coords = sorted(coords, key=lambda element: (element[0], element[1]))

almost_full_space = []
for coord in sorted_coords:
    for second in sorted_coords:
        almost_full_space.append((coord[0], coord[1], second[0], second[1]))

full_space = []
for coord in almost_full_space:
    mi, ma = bounds(coord[0], coord[1], coord[2], coord[3], c)
    distance = ma - mi
    for i in range(int(distance / h) + 1):
        full_space.append((coord[0], coord[1], coord[2], coord[3], np.around(mi + i * h, precision)))

print(len(full_space))

