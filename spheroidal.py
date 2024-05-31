from sympy import *

x1, x2, y1, y2, z1, z2, c = symbols("x_1 x_2 y_1 y_2 z_1 z_2 c")
mu1, nu1, mu2, nu2, phi12, phi = symbols("mu_1 nu_1 mu_2 nu_2 phi_{12} phi", positive = True, real = True)

f = Function('f')(r1, s1, r2, s2, t, a)

def r_trans(car):
    return sqrt((car[0]+c)**2+car[1]**2+car[2]**2).expand()
def s_trans(car):
    return sqrt((car[0]+c)**2+car[1]**2+car[2]**2).expand()
t_trans = sqrt((x1-x2)**2+(y1-y2)**2+(z1-z2)**2).expand()

phi = atan(y1/x1)
phi12 = phi - atan(y2/x2)



car = [[x1, y1, z1], [x2, y2, z2]]

def first(trans, x):
    soln = 0
    for i in range(2):
        for j in range(3):
            cartesian = car[i]
            soln += diff(trans, cartesian[j], cartesian[j])
    return soln.simplify().subs([(trans, x)])

def second(trans):
    soln = 0
    for i in range(2):
        for j in range(3):
            cartesian = car[i]
            soln += diff(trans, cartesian[j])**2
    return soln.simplify()

def mixed(trans1, trans2):
    soln = 0
    for i in range(2):
        for j in range(3):
            cartesian = car[i]
            soln += 2 * diff(trans1, cartesian[j]) * diff(trans2, cartesian[j])
    return soln.simplify()

def full():
    return first(r_trans(car[0]), r1) * Derivative(f, r1) + \
           first(s_trans(car[0]), s1) * Derivative(f, s1) + \
           first(r_trans(car[1]), r2) * Derivative(f, r2) + \
           first(s_trans(car[1]), s2) * Derivative(f, s2) + \
           first(t_trans, t) * Derivative(f, t) + \
           second(r_trans(car[0])) * Derivative(f, r1, r1) + \
           second(s_trans(car[0])) * Derivative(f, s1, s1) + \
           second(r_trans(car[1])) * Derivative(f, r2, r2) + \
           second(s_trans(car[1])) * Derivative(f, s2, s2) + \
           second(t_trans) * Derivative(f, t, t) + \
           mixed(r_trans(car[0]), s_trans(car[0])) * Derivative(f, r1, s1) + \
           mixed(r_trans(car[1]), s_trans(car[1])) * Derivative(f, r2, s2) + \
           mixed(t_trans, s_trans(car[1])).simplify().subs([(r_trans(car[1]), r2), (t_trans, t)]).factor().subs([((-t_trans**2 + s_trans(car[0])**2 - s_trans(car[1])**2) / 2, (-t**2 + s1**2 - s2**2) / 2)]).simplify() * Derivative(f, s1, t) + \
           mixed(t_trans, s_trans(car[0])).simplify().subs([(r_trans(car[0]), r1), (t_trans, t)]).factor().subs([((t_trans**2 + s_trans(car[0])**2 - s_trans(car[1])**2) / 2, (t**2 + s1**2 - s2**2) / 2)]).simplify() * Derivative(f, s1, t) + \
           mixed(t_trans, r_trans(car[0])).simplify().subs([(r_trans(car[0]), r1), (t_trans, t)]).factor().subs([((t_trans**2 + r_trans(car[0])**2 - r_trans(car[1])**2) / 2, (t**2 + r1**2 - r2**2) / 2)]).simplify() * Derivative(f, r1, t) + \
           mixed(t_trans, r_trans(car[1])).simplify().subs([(r_trans(car[1]), r2), (t_trans, t)]).factor().subs([((t_trans**2 + r_trans(car[1])**2 - r_trans(car[0])**2) / 2, (t**2 + r2**2 - r1**2) / 2)]).simplify() * Derivative(f, r2, t)

phi = acos(y1/sqrt(y1**2+z1**2))
soln = first(phi, a)
soln = second(phi).subs([(y1**2+z1**2, r1**2-((r1**2-s1**2)/4/c + c)**2)]).simplify()
soln = mixed(phi, t_trans).simplify()

preview(soln, output='png', viewer='feh')

#preview(full().subs(f, Symbol('')), output='png', viewer='feh')
#print(latex((full_laplace(x1, y1, z1, r1, s1, r1_trans, s1_trans, x2, y2, z2, r2, s2, r2_trans, s2_trans) +\
#            full_laplace(x2, y2, z2, r2, s2, r2_trans, s2_trans, x1, y1, z1, r1, s1, r1_trans, s1_trans))simplify().subs(f,Symbol(''))))
