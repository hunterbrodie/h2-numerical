from sympy import *

x1, x2, y1, y2, z1, z2, c = symbols("x_1 x_2 y_1 y_2 z_1 z_2 c")
r1, s1, r2, s2, t, p, p12 = symbols("r_1 s_1 r_2 s_2 t phi phi_12", positive = True, real = True)

f = Function('f')(r1, s1, r2, s2, p, p12)

def r_trans(car):
    return sqrt((car[0]+c)**2+car[1]**2+car[2]**2).expand()
def s_trans(car):
    return sqrt((car[0]+c)**2+car[1]**2+car[2]**2).expand()
phi = acos(y1/sqrt(y1**2+z1**2))
phi12 = acos(y2/sqrt(y2**2+z2**2)) - acos(y1/sqrt(y1**2+z1**2))

car = [[x1, y1, z1], [x2, y2, z2]]
earthquake = [[r1, s1], [r2, s2]]

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
           second(r_trans(car[0])) * Derivative(f, r1, r1) + \
           second(s_trans(car[0])) * Derivative(f, s1, s1) + \
           second(r_trans(car[1])) * Derivative(f, r2, r2) + \
           second(s_trans(car[1])) * Derivative(f, s2, s2) + \
           mixed(r_trans(car[0]), s_trans(car[0])) * Derivative(f, r1, s1) + \
           mixed(r_trans(car[1]), s_trans(car[1])) * Derivative(f, r2, s2) + \
           first(phi, p) * Derivative(f, p) + \
           first(phi12, p12) * Derivative(f, p12) + \
           second(phi).subs([(y1**2+z1**2, r1**2-((r1**2-s1**2)/4/c+c)**2)]).simplify() * Derivative(f, p, p) + \
           second(phi12).factor().subs([(y1**2+z1**2, r1**2-((r1**2-s1**2)/4/c+c)**2)]).subs([(y2**2+z2**2, r2**2-((r2**2-s2**2)/4/c+c)**2)]).simplify() * Derivative(f, p12, p12) + \
           mixed(phi, phi12).subs([(y1**2+z1**2, r1**2-((r1**2-s1**2)/4/c+c)**2)]).simplify() * Derivative(f, p, p12) + \
           mixed(phi, r_trans(car[0])) * Derivative(f, r1, p) + \
           mixed(phi, r_trans(car[1])) * Derivative(f, r2, p) + \
           mixed(phi, s_trans(car[0])) * Derivative(f, s1, p) + \
           mixed(phi, s_trans(car[1])) * Derivative(f, s2, p) + \
           mixed(phi12, r_trans(car[0])) * Derivative(f, p12, r1) + \
           mixed(phi12, r_trans(car[1])) * Derivative(f, p12, r2) + \
           mixed(phi12, s_trans(car[0])) * Derivative(f, p12, s1) + \
           mixed(phi12, s_trans(car[1])) * Derivative(f, p12, s2)

preview(full().subs(f, Symbol('')), output='png', viewer='feh')
print(latex(full().simplify().subs(f,Symbol(''))))
